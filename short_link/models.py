import random
import string

from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_id = models.CharField(max_length=10)
    httpurl = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.httpurl

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_id = ''.join(random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase)
                                    for x in range(10))

        return super().save(*args, **kwargs)
