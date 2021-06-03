from django import forms
from .models import Comment
from phonenumber_field.formfields import PhoneNumberField


class CommentForm(forms.ModelForm):
    phone = PhoneNumberField()

    class Meta:
        model = Comment
        fields = ('phone', 'email', 'comment', 'image')
