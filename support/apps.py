from django.apps import AppConfig


class SupportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'support'


class AccountConfig(AppConfig):
    name = 'account'


class InvitationsConfig(AppConfig):
    name = 'pinax.invitations'


class Bootstrap4Config(AppConfig):
    name = 'bootstrap4'
