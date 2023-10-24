import pydantic
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from core.service_layer import register_user_service, \
    login_user_service, serials_list_service, check_auth_service
from core.validators import RegisterUserRequest, \
    RegisterUserVO, \
    LoginUserVO, \
    LoginUserRequest


@require_POST
@csrf_exempt
def register_user_view(request):
    register_user_request = RegisterUserRequest.model_validate_json(request.body)
    register_vo = RegisterUserVO(**register_user_request.model_dump())

    response = register_user_service(request, register_vo)
    return JsonResponse(response)


@require_POST
@csrf_exempt
def login_user_view(request):
    login_user_request_body = LoginUserRequest.model_validate_json(request.body)
    login_vo = LoginUserVO(**login_user_request_body.model_dump())

    login_user_response = login_user_service(request, login_vo)
    return JsonResponse(login_user_response)


@require_GET
# @login_required
@csrf_exempt
def serials_list_view(request, user_id):
    try:
        check_auth_service(request)
    except PermissionDenied:
        return HttpResponse(status=403)
    else:
        return JsonResponse(serials_list_service(user_id), safe=False)
