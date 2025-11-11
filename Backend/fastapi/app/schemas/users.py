from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import desc

class UserCreate(BaseModel):
    username: str = Field(min_length=5, max_length=20, description="Логин пользователя для входа или регистрации в системе")
    fio: str = Field(min_length=15, max_length=50, description="ФИО пользователя", pattern=r'^[а-яА-ЯёЁ]+(?:[\s-][а-яА-ЯёЁ\s-]+$)') #регулярка не моя
    password: str = Field(min_length=5, max_length=20, description="Пароль пользователя")
    
class User(BaseModel):
    id: int 
    username: str
    fio: str
    data_registred: datetime
    is_active: bool
    role: str

    model_config=ConfigDict(from_attributes=True)
