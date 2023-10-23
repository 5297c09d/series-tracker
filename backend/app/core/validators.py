from pydantic import BaseModel


class RegisterUserRequest(BaseModel):
    username: str
    password: str


class LoginUserRequest(BaseModel):
    username: str
    password: str


class RegisterUserResponse(BaseModel):
    user_id: int


class RegisterUserVO(BaseModel):
    username: str
    password: str


class LoginUserVO(BaseModel):
    username: str
    password: str
