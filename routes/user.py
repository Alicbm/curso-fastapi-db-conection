from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import HTMLResponse
from schemas.user import User

user_router = APIRouter()

@user_router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Alic Barandica</h1>')

@user_router.post('/login', tags=['auth'])
def login (user: User):
    if user.email == "admin@mail.com" and user.password == 'admin':
        token: str = create_token(user.dict())
    return token
