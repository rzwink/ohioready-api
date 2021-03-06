# Create your models here.
from auditlog.registry import auditlog
from django.db import models

MEDIA_TYPE = [
    ("www", "www"),
    ("twitter", "twitter"),
    ("youtube", "youtube"),
    ("vimeo", "vimeo"),
    ("image", "image"),
    ("pdf", "pdf"),
]


class Article(models.Model):
    url = models.URLField()
    publisher = models.ForeignKey(
        "Publisher", on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="article")
    media_type = models.CharField(
        max_length=20, choices=MEDIA_TYPE, default=MEDIA_TYPE[0][0]
    )

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if hasattr(self.publisher, "name"):
            return f"{self.publisher.name} - {self.url}"
        else:
            return self.url

    class Meta:
        ordering = ["-created_on", "id"]

    @property
    def formatted_event_title(self):
        if self.event.title:
            if len(self.event.title) > 35:
                return self.event.title[0:33] + "..."
        return self.event.title


auditlog.register(Article)
