from django.test import TestCase

from linksapp.forms import CheckStructureForm


class CheckStructureFormTest(TestCase):

    def test_check_structure_form_field_label(self):
        form = CheckStructureForm()
        self.assertTrue(
            form.fields['check_structure'].label == None or form.fields[
                'check_structure'].label == 'check_structure')

    def test_check_structure_field_help_text(self):
        form = CheckStructureForm()
        self.assertEqual(form.fields['check_structure'].help_text,
                         'enter the data')

    def test_check_structure_field_validation(self):
        data = '{"link": "freestylo.ru", "structure": ' \
               '{"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}'
        form_data = {'renewal_date': data}
        form = CheckStructureForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_check_structure_field_validation_2(self):
        data = '{"link": "https://freestylo.ru", "structure": ' \
               '{"html": 1, "head": 1, "body": 1, "p": 10, "img": 2}}'
        form_data = {'renewal_date': data}
        form = CheckStructureForm(data=form_data)
        self.assertFalse(form.is_valid())
