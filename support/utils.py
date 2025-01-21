import requests
from django.conf import settings


def create_helpdesk_ticket(name, email, message):
    """Создаёт заявку в django-helpdesk через API."""

    url = settings.HELPDESK_API_URL
    headers = {
        'Authorization': f'Token {settings.HELPDESK_API_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        "title": f"Запрос от {name}",
        "queue": settings.HELPDESK_DEFAULT_QUEUE,
        "description": message,
        "submitter_email": email,
        "priority": 3
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(
            f"Ошибка при создании заявки:"
            f"{response.status_code} {response.text}")
