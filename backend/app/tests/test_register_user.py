import pytest
from django.urls import reverse
from django.test import Client

from core.models import User

client = Client()


@pytest.mark.django_db
def test_register_user_view_can_return_response():
    test_username = 'abc'
    test_password = 'abc'
    data = {
        "username": test_username,
        "password": test_password
    }

    response = client.post(reverse('register'), data=data, content_type='application/json')
    test_user = User.objects.get(username=test_username)
    response_user = response.json()["user_id"]

    assert test_user
    assert response.status_code == 200
    assert test_user.id == response_user
    assert response.cookies['sessionid']


@pytest.mark.django_db
def test_login_user_view_can_return_response():
    test_username = 'abc'
    test_password = 'abc'
    test_user = User.objects.create_user(
        username=test_username,
        password=test_password
    )
    test_user.save()
    test_user_id = test_user.id
    data = {
        "username": test_username,
        "password": test_password
    }

    response = client.post(reverse('login'), data=data, content_type='application/json')
    response_user = response.json()["user_id"]

    assert response.status_code == 200
    assert test_user_id == response_user
    assert response.cookies['sessionid']


@pytest.mark.django_db
def test_login_user_view_can_return_error_in_case_user_does_not_exist():
    test_username = 'abc'
    test_password = 'abc'
    data = {
        "username": test_username,
        "password": test_password
    }

    response = client.post(reverse('login'), data=data, content_type='application/json')

    assert response.status_code == 403
    assert response.json()[0] == "user_does_not_exist"
