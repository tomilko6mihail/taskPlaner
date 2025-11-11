from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session

from loguru import logger

from app.config import secret_key, algorythm
from app.models.users import User as UserModel
from app.db_depends import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_MINUTES_EXPIRED = 30
REFRESH_TOKEN_DAYS_EXPIRED = 7 #если понадобится
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='users/token')

def hash_password(password: str):
    print(password, len(password))
    logger.info("Хеширования пароля в БД!")
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    logger.info("Проверка введённого пароля с хешированным в БД!")
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    logger.info("Вход в эндпойнт с созданием access-токена!")
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_MINUTES_EXPIRED)
    to_encode.update({"exp": expire})

    logger.info(f"Был создан access-токен на основе {to_encode}")
    return jwt.encode(to_encode, secret_key, algorithm=algorythm)

def create_refresh_token(data: dict):
    logger.info("Вход в эндпойнт с созданием refresh-токена!")
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_DAYS_EXPIRED)
    to_encode.update({"exp": expire})

    logger.info(f"Был создан refresh-токен на основе {to_encode}")
    return jwt.encode(to_encode, secret_key, algorithm=algorythm)

async def get_current_user(token: str = Depends(oauth2_scheme) ,db: Session = Depends(get_db)):
    logger.info("Вход в эндпойнт проверки пользователя!")
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not valide credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        logger.info("Расшифровываем токен!")
        payload = jwt.decode(token, secret_key, algorithms=algorythm)
        username = payload.get("sub") #ИСПРАВИТЬ  ПОТОМ ЭТУ СТРОЧКУ!!!!!!   
        
        if username is None:
            logger.error("Пользователь не найден в системе!")
            raise credentials_exceptions
    
    except jwt.ExpiredSignatureError:
        logger.error("Срок действия токена истёк!")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired!",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    except jwt.PyJWTError:
        logger.error("Ошибка получения пользователя!")
        raise credentials_exceptions
    
    stmt = select(UserModel).where(UserModel.username == username, UserModel.is_active == True)
    user = db.scalars(stmt).first()

    if user is None:
        logger.error(f"Пользователь с логином={username} не найден в системе и БД!")
        raise credentials_exceptions
    
    logger.info("Получение пользователя прошло успешно!")
    return user

def current_employee(current_employee: UserModel = Depends(get_current_user)):
    logger.info("Проверка пользователя на зарегистрированного!")

    if current_employee.is_employee != True and current_employee.is_active != True:
        logger.error("Данный пользователь не зарегистрирован в системе! В доступе отказано!")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This user is not employee! Only employee and admin can perfom this action!"
        )
    
    logger.info("Проверка пользователя на регистрацию прошла успешно!")
    return current_employee

def get_admin(current_admin: UserModel = Depends(get_current_user)):
    logger.info("Проверяем пользователя на админа!")
    
    if current_admin.is_admin != True and current_admin.is_active != True:
        logger.error("Пользователь не является админом! Отказано в доступе!")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This user is not admin! Only admins can perfom this action!"
        )
    
    return current_admin
