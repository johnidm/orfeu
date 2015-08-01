from rest_framework import serializers

from languages.models import Language

class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ('slug', 'name', 'full_name')



