from fastapi import APIRouter, Depends, Response
from ..schemas import LoginRequest, LoginResponse
from ..dependencies import authenticate_user, create_access_token, get_current_user
from ..models import User

auth_router = APIRouter(prefix="/auth")

@auth_router.post("/login", response_model=LoginResponse)
async def login(login_request: LoginRequest, response: Response, user: User = Depends(authenticate_user)):
    access_token = create_access_token(data={"sub": user.username})
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite='Lax')
    return LoginResponse(username=user.username)

@auth_router.get("/check")
async def check_auth(user: User = Depends(get_current_user)):
    print(user.username)
    return {"username": user.username}