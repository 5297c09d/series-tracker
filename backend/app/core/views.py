import json

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from pydantic import ValidationError

from core.service_layer import register_user_service, \
    login_user_service, \
    serials_list_service, delete_series_service, add_series_service
from validators.validators import RegisterUserRequest, \
    RegisterUserVO, \
    LoginUserRequest, \
    LoginUserVO, \
    SerialsListVO, \
    SerialsListResponse, AddBookmarkRequest, DeleteBookmarkVO, DeleteBookmarkRequest, AddBookmarkVO


@require_POST
@csrf_exempt
def register_user_view(request: WSGIRequest):
    try:
        register_user_request = RegisterUserRequest.model_validate_json(request.body)
        register_vo = RegisterUserVO(**register_user_request.model_dump())
        response = register_user_service(request, register_vo)
        return JsonResponse(response)

    except ObjectDoesNotExist as e:
        return JsonResponse(status=403, data=e.args, safe=False)

    except Exception:
        return JsonResponse(status=500, data={'error': 'unknown_error'}, safe=False)


@require_POST
@csrf_exempt
def login_user_view(request: WSGIRequest):
    try:
        login_user_request = LoginUserRequest.model_validate_json(request.body)
        login_vo = LoginUserVO(**login_user_request.model_dump())
        login_user_response = login_user_service(request, login_vo)
        return JsonResponse(login_user_response)

    except ObjectDoesNotExist as e:
        return JsonResponse(status=403, data=e.args, safe=False)

    except Exception:
        return JsonResponse(status=500, data={'error': 'unknown_error'}, safe=False)


@require_GET
@csrf_exempt
def serials_list_view(request: WSGIRequest, user_id: int):
    try:
        serials_list_vo = SerialsListVO(user_id=user_id)
        response = json.dumps(serials_list_service(request, serials_list_vo))
        serials_list_response = SerialsListResponse.model_validate_json(response)
        serials_list_response = SerialsListResponse.model_dump_json(serials_list_response)
        return JsonResponse(serials_list_response, safe=False)

    except PermissionDenied as e:
        return JsonResponse(status=403, data=e.args, safe=False)

    except Exception:
        return JsonResponse(status=500, data={'error': 'unknown_error'}, safe=False)


@require_http_methods(["PUT", "DELETE"])
@csrf_exempt
def add_or_delete_series_view(request: WSGIRequest, user_id: int, series_id: int):
    if request.method == "PUT":
        try:
            request_body = json.loads(request.body)
            request_body['id'] = series_id
            request_body['owner_id'] = user_id
            add_bookmark_request = AddBookmarkRequest.model_validate(request_body)
            add_bookmark_vo = AddBookmarkVO(**add_bookmark_request.model_dump())
            response = add_series_service(request.user, add_bookmark_vo)
            return JsonResponse(response, safe=False)

        except ObjectDoesNotExist as e:
            return JsonResponse(status=403, data=e.args, safe=False)

        except PermissionDenied as e:
            return JsonResponse(status=403, data=e.args, safe=False)

        except Exception:
            return JsonResponse(status=500, data={'error': 'unknown_error'}, safe=False)

        except ValidationError:
            return JsonResponse(status=500, data={'error': 'validation_error'}, safe=False)

    if request.method == "DELETE":
        try:
            delete_bookmark_vo = DeleteBookmarkVO(id=series_id, owner_id=user_id)
            response = delete_series_service(request.user, delete_bookmark_vo)
            return JsonResponse(response)

        except PermissionDenied as e:
            return JsonResponse(status=403, data=e.args, safe=False)

        except ObjectDoesNotExist as e:
            return JsonResponse(status=403, data=e.args, safe=False)

        except ValidationError:
            return JsonResponse(status=500, data={'error': 'validation_error'}, safe=False)

        except Exception:
            return JsonResponse(status=500, data={'error': 'unknown_error'}, safe=False)
