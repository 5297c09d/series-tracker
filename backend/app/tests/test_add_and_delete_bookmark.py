import uuid

import pytest
from django.urls import reverse
from django.test import Client

from core.models import Bookmark
from tests.factories.factories import user_factory, bookmark_factory

client = Client()


@pytest.mark.django_db
def test_add_series_view_can_invalidate_unauthenticated_user():
    test_user = user_factory()
    test_user_id = test_user.id
    test_bookmark_id = uuid.uuid4()
    test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com/"
    }

    response = client.put(reverse(
        'add_or_delete_series',
        kwargs={
            'user_id': test_user_id,
            'series_id': test_bookmark_id
        }
    ), data=test_bookmark_data, content_type='application/json')

    assert response.status_code == 403
    assert response.json()[0] == "user_is_unauthenticated"


@pytest.mark.django_db
def test_add_series_view_can_invalidate_user_without_permission():
    test_user = user_factory()
    test_bookmark_id = uuid.uuid4()
    test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com/"
    }
    client.force_login(test_user)
    another_user_id = test_user.id + 1

    response = client.put(reverse(
        'add_or_delete_series',
        kwargs={
            'user_id': another_user_id,
            'series_id': test_bookmark_id
        }
    ), data=test_bookmark_data, content_type='application/json')

    assert response.status_code == 403
    assert response.json()[0] == "user_has_no_permission"


@pytest.mark.django_db
def test_add_series_view_can_return_response():
    test_user = user_factory()
    test_bookmark_id = uuid.uuid4()
    test_user_id = test_user.id
    test_bookmark_data = {
        "series_name": "test",
        "series_link": "https://test.com/",
    }
    client.force_login(test_user)

    response = client.put(reverse(
        'add_or_delete_series',
        kwargs={
            'user_id': test_user_id,
            'series_id': test_bookmark_id
        }
    ), data=test_bookmark_data, content_type='application/json')

    test_bookmark = Bookmark.objects.get(
        series_name=test_bookmark_data["series_name"],
        series_link=test_bookmark_data["series_link"]
    )
    response_bookmark_id = response.json()["bookmark_id"]

    assert test_bookmark
    assert response.status_code == 200
    assert str(test_bookmark.id) == response_bookmark_id
    assert str(test_bookmark_id) == response_bookmark_id


def test_add_series_view_in_case_bookmark_already_exists():
    pass


@pytest.mark.django_db
def test_delete_series_view_can_invalidate_unauthenticated_user():
    test_user = user_factory()
    test_bookmark = bookmark_factory(owner_id=test_user.id)

    response = client.delete(reverse(
        'add_or_delete_series',
        kwargs={
            "user_id": test_user.id,
            "series_id": test_bookmark.id
        }
    ), content_type='application/json')

    assert response.status_code == 403
    assert response.json()[0] == "user_is_unauthenticated"


@pytest.mark.django_db
def test_delete_series_view_can_invalidate_user_without_permission():
    test_user = user_factory()
    test_bookmark = bookmark_factory(owner_id=test_user.id)
    client.force_login(test_user)
    another_user_id = test_user.id + 1

    response = client.delete(reverse(
        'add_or_delete_series',
        kwargs={
            'user_id': another_user_id,
            'series_id': test_bookmark.id
        }
    ), content_type='application/json')

    assert response.status_code == 403
    assert response.json()[0] == "user_has_no_permission"


@pytest.mark.django_db
def test_delete_series_view_can_return_response():
    test_user = user_factory()
    test_bookmark = bookmark_factory(owner_id=test_user.id)
    test_bookmark_id = test_bookmark.id
    client.force_login(test_user)

    response = client.delete(reverse(
        'add_or_delete_series',
        kwargs={
            'user_id': test_user.id,
            'series_id': test_bookmark_id
        }
    ), content_type='application/json')

    assert response.status_code == 200
    assert response.json()['response'] == 'bookmark_successfully_deleted'

    with pytest.raises(Bookmark.DoesNotExist):
        Bookmark.objects.get(id=test_bookmark_id)
