# Create your models here.
from auditlog.registry import auditlog
from django.db import models
from django_fsm import FSMField
from django_fsm import transition

IMPACT_AREA = [
    ("Global", "Global"),
    ("National", "National"),
    ("State", "State"),
    ("Columbus", "Columbus"),
    ("Cleveland", "Cleveland"),
    ("Cincinnati", "Cincinnati"),
    ("Dayton", "Dayton"),
]

MEDIA_TYPE = [
    ("www", "www"),
    ("twitter", "twitter"),
    ("youtube", "youtube"),
    ("vimeo", "vimeo"),
    ("image", "image"),
    ("pdf", "pdf"),
]


class Event(models.Model):
    title = models.TextField()

    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    authoritative_url = models.URLField(max_length=1024, null=True, blank=True)

    media_type = models.CharField(
        max_length=20, choices=MEDIA_TYPE, default=MEDIA_TYPE[0][0]
    )
    authorizer = models.ForeignKey("Authorizer", on_delete=models.SET_NULL, null=True)
    scope = models.CharField(
        max_length=32, choices=IMPACT_AREA, default=IMPACT_AREA[0][0]
    )

    tags = models.ManyToManyField("Tag")

    status = FSMField(default="new")

    published_on = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

        def __unicode__(self):
            return self.title

    @transition(field=status, source="new", target="published")
    def publish(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(field=status, source=["new", "published"], target="destroyed")
    def destroy(self):
        """
        Side effects galore
        """


auditlog.register(Event)
