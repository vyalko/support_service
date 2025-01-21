from django.db import models

from . import config


class SupportRequest(models.Model):
    name = models.CharField(
        'Имя',
        max_length=config.MAX_LENGTH_NAME
    )
    email = models.EmailField(
        max_length=config.MAX_LENGTH_NAME
    )
    subject = models.CharField(
        'Тема обращения',
        max_length=config.MAX_LENGTH_SUBJECT
    )
    message = models.TextField(
        'Сообщение'
    )
    ticket_number = models.CharField(
        'Номер заявки',
        max_length=config.MAX_LENGTH_TICKET,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    def _str__(self):
        return f"{self.subject} ({self.email})"
