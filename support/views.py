from django.http import HttpResponse
from django.shortcuts import render
import requests

from .form import SupportForm
from .models import SupportRequest
from .utils import create_helpdesk_ticket


def index(request):
    return HttpResponse(
        "Добро пожаловать! Здесь можно оставить обращение в поддержку."
        )


def create_ticket(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            support_request = SupportRequest.objects.create(
                name=data['name'],
                email=data['email'],
                subject=data['subject'],
                message=data['message']
            )

            try:
                api_response = create_helpdesk_ticket(
                    name=data['name'],
                    email=data['email'],
                    message=data['message']
                )
                support_request.ticket_number = api_response.get(
                    'ticket_number')
                support_request.save()
                return render(request, 'support/success.html',
                              {'ticket_number': support_request.ticket_number})
            except requests.exceptions.RequestException as e:
                return render(request, 'support/error.html', {'error': str(e)})

        else:
            return render(request, 'support/create_ticket.html', {'form': form})

    else:
        form = SupportForm()
        return render(request, 'support/create_ticket.html', {'form': form})
