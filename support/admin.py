from django.contrib import admin

from .models import SupportRequest


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'created_at'
    )
    search_fields = (
        'name',
        'email',
        'subject'
    )
    list_filter = (
        'email',
    )
