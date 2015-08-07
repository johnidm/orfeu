from django.contrib import admin
from translation.models import Language
from translation.models import Sentence

admin.site.register(Language)
admin.site.register(Sentence)
