from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from loguru import logger
import jwt

from app.db_depends import get_async_db, get_db
from app.models.users import User as UserModel
from app.schemas.users import User as UserSchema, UserCreate
from app.auth import verify_password, hash_password, create_access_token, create_refresh_token
from app.config import secret_key, algorythm

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/', response_model=List[UserSchema], status_code=status.HTTP_200_OK)
async def read_all_users(db: Session = Depends(get_db)):
    logger.info("Эндпоинт для получения списка всех пользователей!")
    stmt = select(UserModel).where(UserModel.is_active == True)
    users = db.scalars(stmt).all()
    # result_users = await db.scalars(stmt)
    # users = result_users.all()
    
    logger.info("Получены активные пользователи из БД")
    return users

@router.post('/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(create_user: UserCreate, db: Session = Depends(get_db)):
    logger.info("Эндпоинт по созданию пользователя!")
    stmt = select(UserModel).where(UserModel.fio == create_user.fio, UserModel.username == create_user.username)
    user = db.scalars(stmt).first()

    if user is not None:
        logger.error(f"User with username={create_user.username} and fio={create_user.fio} already registred in system!")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already registred in system!"
        )
    
    db_user = UserModel(
        username=create_user.username,
        fio=create_user.fio,
        hashed_password=hash_password(create_user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info("Новый пользователь был создан!")
    return db_user

#ПО ХОРОШЕМУ, ЭТО МОЖНО ВООБЩЕ В ОТДЕЛЬНЫЙ РОУТЕР ВЫНЕСТИ, НО ПОКА ЧТО ПУСТЬ ЗДЕСЬ ЧАЛИТСЯ
@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.info("Вход в эндпойнт аутентификации пользователя!")
    stmt = select(UserModel).where(UserModel.username == form_data.username, UserModel.is_active == True)
    user = db.scalars(stmt).first()

    if user is None or not verify_password(form_data.password, user.hashed_password):
        logger.error("Ошибка аутентификации пользователя!")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate" : "Bearer"}
        )
    
    logger.info("Создание access-токена!")
    access_token = create_access_token(data={"sub": user.username, "role": user.role, "id": user.id})

    logger.info("Создание refresh-токена!")
    refresh_token = create_refresh_token(data={"sub": user.username, "role": user.role, "id": user.id})

    logger.info("Все токены успешно созданы и переданы в JSON-формате! Выход из эндпойнта!")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
    
@router.post('/refresh-token')
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    logger.info("Вход в эндпойнт для получения нового access-токена!")

    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not valide credentials!"
    )

    try:
        logger.info("Обработка refresh-токена!")
        payload = jwt.decode(refresh_token, secret_key, algorithms=algorythm)

        username = payload.get("sub")

        if username is None:
            logger.error("Ошибка получения логина или проблема с токеном!")
            raise credentials_exceptions
        
    except jwt.PyJWTError:
        logger.error("Ошибка получения пользователя!")
        raise credentials_exceptions
    
    logger.info("Поиск пользователя по логину в БД!")
    stmt = select(UserModel).where(UserModel.username == username, UserModel.is_active == True)
    user = db.scalars(stmt).first()

    if user is None:
        logger.error("Пользователь не существует или не найден в системе и БД!")
        raise credentials_exceptions
    
    logger.info("Создание нового access-токена!")
    access_token = create_access_token(data={"sub": user.username, "role": user.role, "id": user.id})

    logger.info("Новый access-токен создан и передан в JSON-формате!")
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }