import uuid

from django.contrib.auth.models import User as U
from django.db import models


class User(U):
    pass


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    series_name = models.CharField(max_length=100)
    series_link = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
