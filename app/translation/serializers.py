from rest_framework import serializers

from translation.models import Language
from translation.models import Sentence

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('slug', 'name', 'full_name')


class SentenceSerializer(serializers.ModelSerializer):

    comments = serializers.CharField(allow_blank=True)

    class Meta:
        model = Sentence
        fields = ('phrase', 'translation', 'comments', 'translate_from', 'translate_to')
