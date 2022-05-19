from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "dockerized_django_demo_circleci.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import dockerized_django_demo_circleci.users.signals  # noqa F401
        except ImportError:
            pass
