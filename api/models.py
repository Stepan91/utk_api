from django.db import models


class Picture(models.Model):
    image = models.ImageField(verbose_name='Изображение')
