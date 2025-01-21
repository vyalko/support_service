from django import forms

from . import config


class SupportForm(forms.Form):
    name = forms.CharField(
        max_length=config.MAX_LENGTH_NAME,
        label="Ваше имя",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label="Ваш email",
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    subject = forms.CharField(
        max_length=config.MAX_LENGTH_SUBJECT,
        label="Тема обращения",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 5}
        )
    )
