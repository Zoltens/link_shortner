from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Urls


class ShortForm(ModelForm):
    class Meta:
        model = Urls
        fields = ['httpurl']
        labels = {'httpurl': 'Длинная ссылка'}

