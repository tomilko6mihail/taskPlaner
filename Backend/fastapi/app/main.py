from operator import call
from urllib import response
from fastapi import FastAPI, APIRouter, Request, status
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
import os

from app.routers import users

app = FastAPI(
    title="Планировщик задач на FastAPI",
    version="0.1.0"
)

app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("HOSTS", "default"),
    allow_methods=os.getenv("METHODS", "default"),
    allow_headers=["*"],
    allow_credentials=True
)

logger.add("requests.log", format="[{time} - {level} - {message}]", level="INFO")

@app.middleware("http")
async def custom_middleware_for_logger(request: Request, call_next):
    path=request.url.path
    try:
        response = await call_next(request)
        if response.status_code in [400, 401, 402, 403, 404]:
            logger.warning(f"Request to {path} failed")
        else:
            logger.info(f"Request to {path} successfully accessed!")
    except Exception as ex:
        logger.error(f"Request to {path} failed: {ex}")
        response = JSONResponse(content={"success": False}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response

@app.get('/')
async def read_root():
    return {"message": "Hello World"}