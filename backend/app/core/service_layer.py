
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest

from core.models import User, Bookmark
from validators.validators import LoginUserVO, LoginUserRequest, RegisterUserVO, CheckAuthVO, SerialsListVO


def register_user_service(request: WSGIRequest, register_user_vo: RegisterUserVO):
    user = User.objects.create_user(
        username=register_user_vo.username,
        password=register_user_vo.password
    )
    user.save()
    login_user_request = LoginUserRequest.model_validate_json(request.body)
    login_vo = LoginUserVO(**login_user_request.model_dump())
    login_user_response = login_user_service(request, login_vo)
    return login_user_response


def login_user_service(request: WSGIRequest, login_user_vo: LoginUserVO):
    user = authenticate(
        request=request,
        username=login_user_vo.username,
        password=login_user_vo.password
    )
    if user is not None:
        login(request, user)
        return {'user_id': user.id}
    raise User.DoesNotExist("user_does_not_exist")


def serials_list_service(request: WSGIRequest, user_id: SerialsListVO):
    validate_auth_service(request.user)
    if request.user.id != user_id.user_id:
        raise PermissionDenied("user_has_no_permission")
    serials_query = list(Bookmark.objects.filter(owner=user_id.user_id).values())
    return serials_query


def validate_auth_service(user: User):
    if not user.is_authenticated:
        raise PermissionDenied("user_is_unauthenticated")
