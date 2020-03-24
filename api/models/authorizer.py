# Create your models here.
from auditlog.registry import auditlog
from django.db import models


class Authorizer(models.Model):
    name = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


auditlog.register(Authorizer)
