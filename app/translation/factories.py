import factory
import factory.fuzzy
from translation.models import Language


class LanguageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Language

    name = '{0}-{1}'.format(factory.fuzzy.FuzzyText(length=2), factory.fuzzy.FuzzyText(length=2))
    full_name = '{0} - {1}'.format(factory.fuzzy.FuzzyText(), factory.fuzzy.FuzzyText())


