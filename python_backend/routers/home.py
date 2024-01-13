from fastapi import APIRouter, HTTPException, Depends, Response
from ..dependencies import get_current_user
from ..models import User

home_router = APIRouter(prefix="/")

@home_router.get("/")
async def get_home(user: User = Depends(get_current_user)):
    return 