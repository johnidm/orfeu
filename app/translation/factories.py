import factory


class LanguageFactory(factory.Factory):

    class Meta:
        model = 'translation.Language'

    name = '{0}-{1}'.format(factory.fuzzy.FuzzyText(length=2), factory.fuzzy.FuzzyText(length=2))
    full_name = '{0} - {1}'.format(factory.fuzzy.FuzzyText(), factory.fuzzy.FuzzyText())


