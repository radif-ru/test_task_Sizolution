from django import forms

from authapp.models import SizolutionUser


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'check_structure'


class CheckStructureForm(FormControlMixin, forms.Form):
    check_structure = forms.CharField(max_length=1000)
