from auditlog.registry import auditlog
from django.db import models


class Breakout(models.Model):
    cases = models.IntegerField()
    deaths = models.IntegerField()
    county = models.ForeignKey("County", on_delete=models.CASCADE)
    source = models.ForeignKey("Authorizer", on_delete=models.CASCADE)
    as_of = models.DateField()

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "as_of",
            "county__name",
        ]
        unique_together = [["county", "as_of"]]

    def __str__(self):
        return f"{self.as_of} {self.county.name}"


auditlog.register(Breakout)
