from django import forms

from .models import Urls


class ShortForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ['httpurl']
        labels = {'httpurl': 'Вставьте вашу ссылку'}
