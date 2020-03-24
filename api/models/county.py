from auditlog.registry import auditlog
from django.db import models


class County(models.Model):
    name = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "counties"

    def __str__(self):
        return self.name


auditlog.register(County)
