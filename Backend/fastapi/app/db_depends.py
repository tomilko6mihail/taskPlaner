from app.db import session_maker
from sqlalchemy.orm import Session

#========================================Синхронное подключение================================
def get_db():
    db: Session = session_maker()
    try: 
        yield db
    finally:
        db.close()


#=====================================Асинхронное подключение==================================
from collections.abc import AsyncGenerator
from app.db import async_session_maker

async def get_async_db():
    async with async_session_maker() as session:
        yield session