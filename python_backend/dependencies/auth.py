from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .database_connector import DbConnector
from ..schemas import LoginRequest
from ..models import User

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def authenticate_user(login_request: LoginRequest, db_connector: DbConnector = Depends()) -> User:
    user = await db_connector.get_user(login_request.username)
    if not user or not pwd_context.verify(login_request.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(request: Request, db_connector: DbConnector = Depends()) -> User:
    token = request.cookies.get("access_token")
    print(token)
    if not token:
        raise HTTPException(status_code=401, detail="Authentication credentials were not provided")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        user = await db_connector.get_user(username)
        if user is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
