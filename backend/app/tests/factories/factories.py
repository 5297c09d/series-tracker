import uuid

from core.models import User, Bookmark


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
        "id": str(uuid.uuid4()),
        "series_name": "test",
        "series_link": "https://test.com/",
        "owner_id": 1
    }
    default_test_bookmark_data.update(kwargs)
    test_bookmark = Bookmark.objects.create(
        id=default_test_bookmark_data['id'],
        series_name=default_test_bookmark_data['series_name'],
        series_link=default_test_bookmark_data['series_link'],
        owner_id=default_test_bookmark_data['owner_id']
    )
    test_bookmark.save()
    return test_bookmark
