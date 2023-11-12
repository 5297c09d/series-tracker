from uuid import UUID

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
    id: UUID
    series_name: str
    series_link: AnyHttpUrl
    owner_id: int


class SerialsListResponse(RootModel):
    root: list[SerialsListResponseItem]


class AddBookmarkRequest(BaseModel):
    id: UUID
    series_name: str
    series_link: AnyHttpUrl
    owner_id: int


class AddBookmarkVO(BaseModel):
    id: UUID
    series_name: str
    series_link: AnyHttpUrl
    owner_id: int


class DeleteBookmarkRequest(BaseModel):
    id: UUID
    owner_id: int


class DeleteBookmarkVO(BaseModel):
    id: UUID
    owner_id: int
