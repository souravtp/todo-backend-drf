from django.db import models

from account.models import CustomUser


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
