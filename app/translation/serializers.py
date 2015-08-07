from rest_framework import serializers

from translation.models import Language

class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ('slug', 'name', 'full_name')



