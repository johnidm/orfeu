from django.test import TestCase

from translation.factories import LanguageFactory
from translation.factories import SentenceFactory


from rest_framework import status
from rest_framework.test import APITestCase


class SentenceTests(TestCase):

    def test_str(self):

        phrase = "How are you?"
        sentence = SentenceFactory.create(phrase=phrase)

        actual = str(sentence)
        expected = '{0} to {1} - {2}'.format(sentence.translate_from.name,
                                             sentence.translate_to.name, phrase)

        self.assertEquals(actual, expected)


class SentenceAPITests(APITestCase):

    def setUp(self):

        self.translate_pt_BR = LanguageFactory.create(
            name='pt-BR', full_name='Portuguese - Brasil')
        self.translate_us_EN = LanguageFactory.create(
            name='en-US', full_name='English - United States')

        self.sentence = SentenceFactory.create(
            phrase='You can do anything, but not everything.',
            translation='Você pode fazer qualquer coisa, mas não tudo.',
            comments='',
            translate_to=self.translate_us_EN,
            translate_from=self.translate_pt_BR)

        self.url = '/api/sentence/'
        self.url_detail = '{}{}/'.format(self.url, self.sentence.id)

    def test_create_sentence(self):

        data = {
            'phrase': 'Eles virão esta noite?',
            'translation': 'Are they coming this evening?',
            'comments': '',
            'translate_from': self.translate_us_EN.id,
            'translate_to': self.translate_pt_BR.id,
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['phrase'], data['phrase'])
        self.assertEqual(response.data['translation'], data['translation'])
        self.assertEqual(response.data['comments'], data['comments'])
        self.assertEqual(response.data['translate_from'], self.translate_us_EN.id)
        self.assertEqual(response.data['translate_to'], self.translate_pt_BR.id)

    def test_get_all_sentences(self):

        SentenceFactory.create()

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['phrase'], self.sentence.phrase)
        self.assertEqual(
            response.data[0]['translation'], self.sentence.translation)
        self.assertEqual(response.data[0]['comments'], '')
        self.assertEqual(
            response.data[0]['translate_from'], self.translate_pt_BR.id)
        self.assertEqual(
            response.data[0]['translate_to'], self.translate_us_EN.id)


class LanguageModelTests(TestCase):

    def test_str(self):
        language = LanguageFactory.create(
            name='pt-BR', full_name='Portuguese - Brasil')

        actual = str(language)
        expected = 'Portuguese - Brasil (pt-BR)'
        self.assertEquals(actual, expected)

    def test_slug(self):
        language = LanguageFactory.create(
            name='en-US', full_name='English - United States')

        actual = language.slug

        expected = 'en-us'
        self.assertEquals(actual, expected)


class LanguageAPITests(APITestCase):

    def setUp(self):
        self.language = LanguageFactory.create(
            name='en-US', full_name='English - United States')

        self.url = '/api/language/'
        self.url_detail = '{}{}/'.format(self.url, self.language.id)

    def test_get_all_languages(self):

        LanguageFactory.create(name='pt-BR', full_name='Portuguese - Brazil')

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['slug'], 'en-us')
        self.assertEqual(response.data[0]['name'], 'en-US')
        self.assertEqual(
            response.data[0]['full_name'], 'English - United States')

        self.assertEqual(response.data[1]['slug'], 'pt-br')
        self.assertEqual(response.data[1]['name'], 'pt-BR')
        self.assertEqual(response.data[1]['full_name'], 'Portuguese - Brazil')

    def test_update_all_felds(self):

        data = {
            'name': 'en-BZ',
            'full_name': 'English - Belize',
        }

        response = self.client.patch(self.url_detail, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['slug'], 'en-bz')
        self.assertEqual(response.data['name'], 'en-BZ')
        self.assertEqual(response.data['full_name'], 'English - Belize')

    def test_update_langauge_full_name(self):
        data = {'full_name': 'English - EUA'}

        response = self.client.patch(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.url_detail, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['slug'], 'en-us')
        self.assertEqual(response.data['name'], 'en-US')
        self.assertEqual(response.data['full_name'], 'English - EUA')

    def test_update_langauge_name(self):
        data = {'name': 'en-UR'}

        response = self.client.patch(self.url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.url_detail, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['slug'], 'en-ur')
        self.assertEqual(response.data['name'], 'en-UR')
        self.assertEqual(response.data['full_name'], 'English - United States')

    def test_delete_language(self):
        response = self.client.delete(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_language(self):

        data = {
            'name': 'en-BZ',
            'full_name': 'English - Belize',
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['slug'], 'en-bz')
        self.assertEqual(response.data['name'], 'en-BZ')
        self.assertEqual(response.data['full_name'], 'English - Belize')

    def test_get_language(self):

        response = self.client.get(self.url_detail, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['slug'], 'en-us')
        self.assertEqual(response.data['name'], 'en-US')
        self.assertEqual(response.data['full_name'], 'English - United States')
