# Create your models here.
from auditlog.registry import auditlog
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

TYPE = [
    ("STATE", "State"),
    ("GLOBAL", "Global"),
    ("NATIONAL", "National"),
    ("LOCAL", "Local"),
]


class Publisher(models.Model):
    name = models.TextField(unique=True)
    homepage_url = models.URLField()
    type = models.CharField(max_length=32, choices=TYPE, default=TYPE[0])
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "id"]

    @property
    def popularity(self):
        return self.articles.count()


auditlog.register(Publisher)
