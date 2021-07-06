from django.test import TestCase

# Create your tests here.

from authapp.models import SizolutionUser as User


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            phone_number='+79276243641',
            phone_code=
            '416578F81246A2A44CA12C455FBCB953A47808D92F041ADA3B6E700B805FB10F'
        )

    def test_phone_number_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'номер телефона')

    def test_phone_code_label(self):
        author = User.objects.get(id=1)
        field_label = author._meta.get_field('phone_code').verbose_name
        self.assertEquals(field_label, 'код телефона')

    def test_phone_number_max_length(self):
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 18)

    def test_phone_code_max_length(self):
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('phone_code').max_length
        self.assertEquals(max_length, 64)
