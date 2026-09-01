from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, Token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    return UserResponse(id=101, email=user.email, full_name=user.full_name)

@router.post("/login", response_model=Token)
async def login(user: UserCreate):
    if user.email == "demo@example.com" and user.password == "password":
        return Token(access_token="fake-jwt-token-sample")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
