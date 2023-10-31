import json

import pytest
from unittest import mock
from django.urls import reverse
from django.test import Client

from core.models import User, Bookmark

client = Client()


@pytest.mark.django_db
def test_series_list_view_can_invalidate_unauthenticated_user():
    test_user = user_factory()

    response = client.get(reverse('serials', kwargs={'user_id': test_user.id}))

    print(response)
    print(response.json())
    # print(json.loads(response.json()))

    assert response.status_code == 403
    assert response.json()[0] == "user_is_unauthenticated"


@pytest.mark.django_db
def test_series_list_view_can_invalidate_user_without_permission():
    test_user = user_factory()
    client.force_login(test_user)
    another_user_id = test_user.id + 1

    response = client.get(reverse('serials', kwargs={'user_id': another_user_id}))
    assert response.status_code == 403
    assert response.json()[0] == "user_has_no_permission"


@pytest.mark.django_db
def test_series_list_view_can_return_user_series():
    test_user = user_factory()
    test_bookmark = bookmark_factory(owner_id=test_user.id)
    client.force_login(test_user)
    mock_response = {
        '_state': mock.ANY,
        'id': mock.ANY,
    }

    response = client.get(reverse('serials', kwargs={'user_id': test_user.id}))

    assert response.status_code == 200
    response = json.loads(response.json())
    mock_response.update(response[0])
    assert mock_response == test_bookmark.__dict__


@pytest.mark.django_db
def test_series_list_view_can_return_empty_list_in_case_of_no_series():
    # test_bookmark.delete()
    test_user = user_factory()
    client.force_login(test_user)

    empty_response = client.get(reverse('serials', kwargs={'user_id': test_user.id}))

    assert empty_response.status_code == 200
    empty_response = json.loads(empty_response.json())
    assert len(empty_response) == 0


def user_factory(**kwargs):
    default_test_user_data = {
        "username": 'abc',
        "password": 'abc'
    }
    default_test_user_data.update(kwargs)
    test_user = User.objects.create_user(
        username=default_test_user_data['username'],
        password=default_test_user_data['password']
    )
    test_user.save()
    return test_user


def bookmark_factory(**kwargs):
    default_test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com/",
        "owner_id": 1
    }
    default_test_bookmark_data.update(kwargs)
    test_bookmark = Bookmark.objects.create(
        series_name=default_test_bookmark_data['series_name'],
        series_link=default_test_bookmark_data['series_link'],
        owner_id=default_test_bookmark_data['owner_id']
    )
    test_bookmark.save()
    return test_bookmark
