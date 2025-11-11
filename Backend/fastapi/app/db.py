from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#======================================Синхронное подключение===================================

engine_sync = create_engine("sqlite:///taskPlaner.db", echo=True)

session_maker = sessionmaker(bind=engine_sync)

#==============================Асинхронное подключение к гренке==================================
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("postgresql+asyncpg:///localhost:5432/postgres", echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass   

