import requests
from django.test import TestCase

from authapp.models import SizolutionUser as User
from linksapp.views import correct_url


class AuthAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            phone_number='+79276243641',
            phone_code=
            '416578F81246A2A44CA12C455FBCB953A47808D92F041ADA3B6E700B805FB10F'
        )

    def test_correct_url_func(self):
        urls = ['freestylo.ru', 'http://freestylo.ru', 'https://freestylo.ru',
                'ya.ru', 'google.com', 'habr.com']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) '
                          'Gecko/20100101 Firefox/89.0 '
        }
        for url in urls:
            response = requests.get(url=correct_url(url), headers=headers)
            self.assertEqual(response.status_code, 200)

    # TODO: разобраться с Selenium, мешает тестам
    # def test_view_url_exists_structure(self):
    #     resp = self.client.get('/structure?link=freestylo.ru&tags=html,img')
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_view_url_exists_check_structure_add_post(self):
    #     data = '{"link": "freestylo.ru", "structure": ' \
    #            '{"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}'
    #     resp = self.client.post(
    #         '/check_structure ', data=data)
    #     self.assertEqual(resp.status_code, 200)
