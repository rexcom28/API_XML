from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ProfilesConfig(AppConfig):
    name = 'Profiles'
    verbose_name = _('profiles')
    def ready(self):
        import Profiles.signals