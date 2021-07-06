from django.test import TestCase

# Create your tests here.

from authapp.models import SizolutionUser as User

from authapp.views import correct_num, phone_code_generate, code_encryption


class AuthAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            phone_number='+79276243641',
            phone_code=
            '416578F81246A2A44CA12C455FBCB953A47808D92F041ADA3B6E700B805FB10F'
        )

    def test_view_url_exists_login(self):
        resp = self.client.get('/login')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_login_add_post(self):
        resp = self.client.post(
            '/login', data={"phone": "+79276243641", "code": "DKGYDN"})
        self.assertEqual(resp.status_code, 200)

    def test_correct_num_func(self):
        nums = ['89054234326', ' 79276243641', '+7963521756']
        for num in nums:
            self.assertFalse(correct_num(num[0]) == ' ')

    def test_phone_code_generate_func(self):
        for num in range(10):
            self.assertTrue(len(phone_code_generate(num)) == num)

    def test_code_encryption_func(self):
        nums = ['89054234326', ' 79276243641', '+7963521756']
        for num in nums:
            self.assertTrue(len(code_encryption(num)) == 64)
