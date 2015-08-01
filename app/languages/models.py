from django.db import models
from autoslug import AutoSlugField

class Language(models.Model):

    name = models.CharField(max_length=6, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=40, unique=True, null=False, blank=False)
    slug = AutoSlugField(max_length=6, populate_from='name', unique=True, always_update =True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.full_name, self.name)

