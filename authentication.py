from urllib.request import HTTPBasicAuthHandler
from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException
from users import users_db

security = HTTPBasicAuthHandler()

def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password

def get_user(username: str):
    if username in users_db:
        return users_db[username]
    return None

def authenticate_user(credentials: HTTPBasicCredentials):
    username = credentials.username
    password = credentials.password
    
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    return username
