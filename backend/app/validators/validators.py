from pydantic import BaseModel, AnyHttpUrl, RootModel


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


class SerialsListRequest(BaseModel):
    is_authenticated: bool


class CheckAuthVO(BaseModel):
    is_authenticated: bool


class SerialsListVO(BaseModel):
    user_id: int


class SerialsListResponseItem(BaseModel):
    series_name: str
    series_link: AnyHttpUrl
    owner_id: int


class SerialsListResponse(RootModel):
    root: list[SerialsListResponseItem]
