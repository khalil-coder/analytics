from django.apps import AppConfig
import posthog


class HoggerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hogger"
    verbose_name = "Hogger"

    def ready(self):
        posthog.api_key = "phc_7G5P78SjtOI9s2ybkbp7Lvy16LR3b6UUvprEZ12Gu3v"
        posthog.host = "https://us.i.posthog.com"
