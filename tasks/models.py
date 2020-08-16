from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, default='')
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('user', 'title',)

