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

    test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com",
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
    response = client.get(reverse('serials', kwargs={'user_id': test_user_id}))

    assert response.status_code == 200
    assert response.json()
    assert test_bookmark_data['series_name'] == response.json()[0]['series_name']
    assert test_bookmark_data['series_link'] == response.json()[0]['series_link']
    assert test_bookmark_data['owner_id'] == response.json()[0]['owner_id']
