from django.db import models
from django.contrib.sites.models import Site

from lib.sitestuff import SiteModel


class Topic(models.Model):
    display_name = models.CharField(max_length=50)
    internal_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{} <{}>'.format(self.display_name, self.internal_name)


class RelatedDive(SiteModel):
    related_dive = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='related_dives')

    class Meta:
        unique_together = ('site', 'related_dive')
