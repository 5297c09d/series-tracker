import json

from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from core.service_layer import register_user_service, \
                               login_user_service, \
                               serials_list_service
from validators.validators import RegisterUserRequest, \
                               RegisterUserVO, \
                               LoginUserRequest, \
                               LoginUserVO, \
                               SerialsListVO, \
                               SerialsListResponse


@require_POST
@csrf_exempt
def register_user_view(request: WSGIRequest):
    register_user_request = RegisterUserRequest.model_validate_json(request.body)
    register_vo = RegisterUserVO(**register_user_request.model_dump())

    response = register_user_service(request, register_vo)
    return JsonResponse(response)


@require_POST
@csrf_exempt
def login_user_view(request: WSGIRequest):
    login_user_request = LoginUserRequest.model_validate_json(request.body)
    login_vo = LoginUserVO(**login_user_request.model_dump())

    login_user_response = login_user_service(request, login_vo)
    return JsonResponse(login_user_response)


@require_GET
@csrf_exempt
def serials_list_view(request: WSGIRequest, user_id: int):
    serials_list_vo = SerialsListVO(user_id=user_id)
    try:
        response = json.dumps(serials_list_service(request, serials_list_vo))
    except PermissionDenied:
        return HttpResponse(status=403)
    if isinstance(response, HttpResponse):
        return response
    else:
        serials_list_response = SerialsListResponse.model_validate_json(response)
        serials_list_response = SerialsListResponse.model_dump_json(serials_list_response)
        return JsonResponse(serials_list_response, safe=False)
