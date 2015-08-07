from rest_framework import viewsets

from translation.models import Language
from translation.models import Sentence

from translation.serializers import LanguageSerializer
from translation.serializers import SentenceSerializer


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


class SentenceViewSet(viewsets.ModelViewSet):
	queryset = Sentence.objects.order_by('created_at')
	serializer_class = SentenceSerializer
