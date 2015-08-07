import factory
import factory.fuzzy

from translation.models import Language
from translation.models import Sentence

from translation.utils import Util



class LanguageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Language

    name = factory.fuzzy.FuzzyText(length=4)
    full_name = factory.fuzzy.FuzzyText(length=15)

class SentenceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Sentence

    translate_from = factory.SubFactory(LanguageFactory)
    translate_to = factory.SubFactory(LanguageFactory)

    phrase = factory.fuzzy.FuzzyText(length=15)
    translation = factory.fuzzy.FuzzyText(length=20)

    comments = factory.fuzzy.FuzzyText(length=100)


