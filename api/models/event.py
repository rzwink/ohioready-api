# Create your models here.
from auditlog.registry import auditlog
from django.db import models
from django.template.defaultfilters import slugify
from django_fsm import FSMField
from django_fsm import transition
from taggit.managers import TaggableManager

IMPACT_AREA = [
    ("STATE", "State"),
    ("GLOBAL", "Global"),
    ("NATIONAL", "National"),
    ("LOCAL", "Local"),
]


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    authoritative_url = models.URLField(null=True, blank=True)
    authoritative_publisher = models.ForeignKey(
        "Publisher", on_delete=models.SET_NULL, null=True, blank=True
    )

    authorizer = models.ForeignKey("Authorizer", on_delete=models.SET_NULL, null=True)
    impact_area = models.CharField(
        max_length=32, choices=IMPACT_AREA, default=IMPACT_AREA[0]
    )

    tags = models.ManyToManyField("Tag")

    status = FSMField(default="new")

    published_on = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ["created_on"]

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
