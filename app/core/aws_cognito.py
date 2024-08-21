import boto3

from ..models.user_model import UserSignup
from .config import env_vars

AWS_REGION_NAME = env_vars.AWS_REGION_NAME
AWS_COGNITO_APP_CLIENT_ID = env_vars.AWS_COGNITO_APP_CLIENT_ID
AWS_COGNITO_USER_POOL_ID = env_vars.AWS_COGNITO_USER_POOL_ID

class AWS_Cognito:
    def __init__(self):
        self.client = boto3.client("cognito-idp", region_name=AWS_REGION_NAME)

    def user_signup(self, user: UserSignup):
        response = self.client.sign_up(
            ClientId=AWS_COGNITO_APP_CLIENT_ID,
            Username=user.email,
            Password=user.password,
            UserAttributes=[
                {
                    'Name': 'name',
                    'Value': user.full_name,
                },
                {
                    'Name': 'phone_number',
                    'Value': user.phone_number
                },
                {
                    'Name': 'custom:role',
                    'Value': user.role
                }
            ],
        )

        return response

    # def verify_account():

    # def user_signin():
    #...
