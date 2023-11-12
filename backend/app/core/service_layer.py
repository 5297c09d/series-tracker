from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest

from core.models import User, Bookmark
from validators.validators import LoginUserVO, LoginUserRequest, RegisterUserVO, CheckAuthVO, SerialsListVO, \
    AddBookmarkVO, DeleteBookmarkVO


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
    for serial in serials_query:
        serial['id'] = str(serial['id'])
    return serials_query


def validate_auth_service(user: User):
    if not user.is_authenticated:
        raise PermissionDenied("user_is_unauthenticated")


def add_series_service(user: User, add_bookmark_vo: AddBookmarkVO):
    validate_auth_service(user)
    if user.id != add_bookmark_vo.owner_id:
        raise PermissionDenied("user_has_no_permission")
    bookmark = Bookmark.objects.create(
        id=add_bookmark_vo.id,
        series_name=add_bookmark_vo.series_name,
        series_link=add_bookmark_vo.series_link,
        owner_id=add_bookmark_vo.owner_id
    )
    bookmark.save()
    return {'bookmark_id': bookmark.id}


def delete_series_service(user: User, delete_bookmark_vo: DeleteBookmarkVO):
    validate_auth_service(user)
    if user.id != delete_bookmark_vo.owner_id:
        raise PermissionDenied("user_has_no_permission")
    bookmark = Bookmark.objects.filter(
        id=delete_bookmark_vo.id
    )
    if bookmark is not None:
        bookmark.delete()
        return {'response': 'bookmark_successfully_deleted'}
    raise Bookmark.DoesNotExist("bookmark_does_not_exist")

