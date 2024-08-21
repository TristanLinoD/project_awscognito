from fastapi import HTTPException
from fastapi.responses import JSONResponse
import botocore

from ..core.aws_cognito import AWS_Cognito
from ..models.user_model import UserSignup

class AuthService:
    def user_signup(user: UserSignup, cognito: AWS_Cognito):
        try:
            response = cognito.user_signup(user)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'UsernameExistsException':
                raise HTTPException(
                    status_code=409, detail="An account with the given email already exists")
            else:
                raise HTTPException(status_code=500, detail=f"{e}")
        else:
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                content = {
                    "message": "User created successfully",
                    "sub": response["UserSub"]
                }
                return JSONResponse(content=content, status_code=201)

    # def user_verify(data: UserVerify, cognito: AWS_Cognito):
    # def user_signin(data: UserSign, cognito: AWS_Cognito):
