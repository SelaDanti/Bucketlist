#api/models
from django.contrib.auth.models import AbstractUser
from django.db import models

class ToDoList(models.Model):
    """This is a representation of buckectlist model."""
    item_name = models.CharField(max_length=200, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    complete=models.BooleanField(default=False)

    def __str__(self):
        """Readable Output for users."""
        return "{}".format(self.item_name)

class CustomUser(AbstractUser):
    name = models.CharField(blank=True,max_length=255)


    def __str__(self):
        return self.email