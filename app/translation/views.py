from rest_framework import viewsets

from translation.models import Language
from translation.serializers import LanguageSerializer


'''
TODO
not allowed HTTP methods

- List
	* DELETE
	* PUT
	* PATCH

- detail
	* PUT
	* POST
'''

class LanguageViewSet(viewsets.ModelViewSet):
	queryset = Language.objects.order_by('created_at')
	serializer_class = LanguageSerializer
