import pydantic
from django.contrib.auth import authenticate, login
from django.core.handlers.wsgi import WSGIRequest

from polls.models import User


class RegisterUserVO(pydantic.BaseModel):
    username: str
    password: str


class LoginUserVO(pydantic.BaseModel):
    username: str
    password: str


def register_user_service(register_user_vo: RegisterUserVO):
    user = User.objects.create_user(
        username=register_user_vo.username,
        password=register_user_vo.password
    )
    user.save()
    return user


def login_user_service(request: WSGIRequest, login_user_vo: LoginUserVO):
    user = authenticate(
        request=request,
        username=login_user_vo.username,
        password=login_user_vo.password
    )
    if user is not None:
        login(request, user)
        return {'user_id': user.id}
    return None
