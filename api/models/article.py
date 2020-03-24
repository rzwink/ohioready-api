# Create your models here.
from auditlog.registry import auditlog
from django.db import models


class Article(models.Model):
    url = models.URLField()
    publisher = models.ForeignKey("Publisher", on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="article")

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.publisher.name} - {self.url}"


auditlog.register(Article)
