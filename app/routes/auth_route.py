from fastapi import APIRouter, status, Depends

from ..models.user_model import UserSignup
from ..services.auth_service import AuthService
from ..core.aws_cognito import AWS_Cognito
from ..core.dependencies import get_aws_cognito

auth_router = APIRouter(prefix='/api/v1/auth')

# USER SIGNUP
@auth_router.post('/signup', status_code=status.HTTP_201_CREATED, tags=['Auth'])
async def signup_user(user: UserSignup, cognito: AWS_Cognito = Depends(get_aws_cognito)):
    return AuthService.user_signup(user, cognito)

# @auth_router.post()
# async def verify_account():

# @auth_router.post()
# async def signin_user():