from django.contrib import admin
from django.urls import path
from polls.views import register_user_view, login_user_view, error_page_view, series_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/login/', login_user_view, name='login'),
    path('api/v1/auth/register/', register_user_view, name='register'),
    path('api/v1/auth/series_page/', series_page_view, name='series_page'),
    path('error/', error_page_view, name='error_page'),
]
