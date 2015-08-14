from django.db import models
from autoslug import AutoSlugField

'''
https://msdn.microsoft.com/en-us/library/ee825488(v=cs.20).aspx
'''

class Language(models.Model):

    name = models.CharField(max_length=6, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=40, unique=True, null=False, blank=False)
    slug = AutoSlugField(max_length=6, populate_from='name', unique=True, always_update =True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.full_name, self.name)


class Sentence(models.Model):

    translate_from = models.ForeignKey(Language, related_name='translate_from', null=False)
    translate_to = models.ForeignKey(Language, related_name='translate_to', null=False)

    phrase = models.CharField(max_length=100, null=False, blank=False)
    translation = models.CharField(max_length=100, null=False, blank=False)

    comments = models.TextField(max_length=500, blank=False, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} to {1} - {2}'.format(self.translate_from.name, self.translate_to.name, self.phrase)