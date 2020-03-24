# Create your models here.
from auditlog.registry import auditlog
from django.db import models


class Coverage(models.Model):
    url = models.URLField()
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)


auditlog.register(Coverage)
