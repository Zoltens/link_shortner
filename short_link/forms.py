from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Urls


class ShortForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ['httpurl']
        labels = {'httpurl': 'Вставьте вашу ссылку'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['httpurl'].widget.attrs.update(
            {'class': 'form-control'}
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )
