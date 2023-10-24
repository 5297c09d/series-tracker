from django.contrib import admin
from django.urls import path
from core.views import register_user_view, login_user_view, serials_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/login/', login_user_view, name='login'),
    path('api/v1/auth/register/', register_user_view, name='register'),
    path('api/v1/users/<int:user_id>/serials/', serials_list_view, name='serials'),
]
