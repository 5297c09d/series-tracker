import json

from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

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
    return User.DoesNotExist


def serials_list_service(request: WSGIRequest, user_id: SerialsListVO):
    try:
        check_auth_service(request)
        if request.user.id != user_id.user_id:
            raise PermissionDenied
    except PermissionDenied:
        return HttpResponse(status=403)
    else:
        serials_query = list(Bookmark.objects.filter(owner=user_id.user_id).values())
        return json.dumps(serials_query)


def check_auth_service(request: WSGIRequest):
    if request.user.is_authenticated:
        return None
    else:
        raise PermissionDenied
