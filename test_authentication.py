from fastapi import HTTPException
from authentication import verify_password, get_user, authenticate_user
from fastapi.security import HTTPBasicCredentials

def test_verify_password():
    hashed_password = "hashed_password1"
    assert verify_password("password", hashed_password) == False
    assert verify_password("password1", hashed_password) == True

def test_get_user():
    assert get_user("employee1") == {"hashed_password": "hashed_password1"}
    assert get_user("employee3") == None

def test_authenticate_user():
    credentials = HTTPBasicCredentials(username="employee1", password="password1")
    assert authenticate_user(credentials) == "employee1"

    credentials = HTTPBasicCredentials(username="employee1", password="password2")
    try:
        authenticate_user(credentials)
    except HTTPException as e:
        assert e.status_code == 401
        assert e.detail == "Неверный логин или пароль"
    else:
        raise AssertionError("Expected HTTPException not raised")

    credentials = HTTPBasicCredentials(username="employee3", password="password1")
    try:
        authenticate_user(credentials)
    except HTTPException as e:
        assert e.status_code == 401
        assert e.detail == "Неверный логин или пароль"
    else:
        raise AssertionError("Expected HTTPException not raised")
