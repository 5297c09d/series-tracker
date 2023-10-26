import json

import pytest
from django.urls import reverse
from django.test import Client

from core.models import User, Bookmark

client = Client()


@pytest.mark.django_db
def test_series_list_view_can_return_response():
    test_user_data = {
        "username": 'abc',
        "password": 'abc'
    }
    test_user = User.objects.create_user(
        username=test_user_data['username'],
        password=test_user_data['password']
    )
    test_user.save()
    test_user_id = test_user.id
    another_user_id = test_user_id + 1

    test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com/",
        "owner_id": test_user.id
    }
    test_bookmark = Bookmark.objects.create(
        series_name=test_bookmark_data['series_name'],
        series_link=test_bookmark_data['series_link'],
        owner_id=test_bookmark_data['owner_id']
    )
    test_bookmark.save()

    response = client.get(reverse('serials', kwargs={'user_id': test_user_id}))
    assert response.status_code == 403

    response = client.post(reverse('login'), data=test_user_data, content_type='application/json')

    response = client.get(reverse('serials', kwargs={'user_id': another_user_id}))
    assert response.status_code == 403

    response = client.get(reverse('serials', kwargs={'user_id': test_user_id}))

    assert response.status_code == 200
    response = json.loads(response.json())
    assert test_bookmark_data['series_name'] == response[0]['series_name']
    assert test_bookmark_data['series_link'] == response[0]['series_link']
    assert test_bookmark_data['owner_id'] == response[0]['owner_id']

    test_bookmark.delete()
    empty_response = client.get(reverse('serials', kwargs={'user_id': test_user_id}))

    assert empty_response.status_code == 200
    empty_response = json.loads(empty_response.json())
    assert len(empty_response) == 0
