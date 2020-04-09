# Create your models here.
from auditlog.registry import auditlog
from django.db import models


class Authorizer(models.Model):
    name = models.TextField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "id"]


auditlog.register(Authorizer)
