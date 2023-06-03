from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasicCredentials
from datetime import datetime, timedelta
import secrets
from authentication import security, authenticate_user
from salary import salary_data, tokens_db

app = FastAPI()

@app.post("/token")
def login(credentials: HTTPBasicCredentials = Depends(authenticate_user)):
    token = secrets.token_hex(16)
    token_expiry = datetime.now() + timedelta(minutes=10)
    tokens_db[token] = credentials
    return {"token": token, "expires_at": token_expiry}

@app.get("/salary")
def get_salary(token: str):
    # Проверка валидности токена
    if token not in tokens_db:
        raise HTTPException(status_code=401, detail="Невалидный токен")
    
    username = tokens_db[token]
    if username not in salary_data:
        raise HTTPException(status_code=404, detail="Данные о зарплате не найдены")

    return salary_data[username]
