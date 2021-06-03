from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Comment(models.Model):
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    email = models.EmailField(
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    comment = models.CharField(max_length=200, verbose_name='Комментарий')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
