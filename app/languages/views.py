from rest_framework import viewsets

from languages.models import Language
from languages.serializers import LanguageSerializer

class LanguageViewSet(viewsets.ModelViewSet):
	queryset = Language.objects.order_by('created_at')
	serializer_class = LanguageSerializer
