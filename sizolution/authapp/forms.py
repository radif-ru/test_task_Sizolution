from django import forms

from authapp.models import SizolutionUser


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'login'


class SizolutionUserForm(FormControlMixin, forms.ModelForm):

    class Meta:
        model = SizolutionUser
        fields = ['phone_number', 'phone_code']
        # exclude = ()
