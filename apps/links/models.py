from django.db import models


class Link(models.Model):
    original_url = models.URLField(max_length=600)
    short_code = models.CharField(max_length=15, blank=True, null=True, unique=True)

    def __str__(self):
        return self.short_code
