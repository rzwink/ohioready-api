from django.db import models


class Screenshot(models.Model):
    name = models.TextField(unique=True)
    file = models.FileField()

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on", "id"]

    def __str__(self):
        return self.name
