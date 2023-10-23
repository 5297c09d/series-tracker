import pydantic

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core.service_layer import register_user_service, \
                               login_user_service
from core.validators import RegisterUserRequest,\
                            RegisterUserVO,\
                            LoginUserVO,\
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
