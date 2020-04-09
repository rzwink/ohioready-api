from auditlog.registry import auditlog
from django.db import models


class Tag(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "id"]


auditlog.register(Tag)
