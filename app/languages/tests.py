from django.test import TestCase
from languages.models import Language

class LanguageTests(TestCase):

	def test_str(self):
		language = Language(name='pt-BR', full_name='Portuguese - Brasil')
		language.save()

		actual = str(language)
		expected = 'Portuguese - Brasil (pt-BR)'
		self.assertEquals(actual, expected)


	def test_slug(self):
		language = Language(name='en-US', full_name='English - United States')
		language.save()

		actual = language.slug

		expected = 'en-us'
		self.assertEquals(actual, expected)

