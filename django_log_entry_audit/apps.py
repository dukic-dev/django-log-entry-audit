from django.apps import AppConfig


class DjangoLogEntryAuditConfig(AppConfig):
    name = "django_log_entry_audit"

    def ready(self):
        import django_log_entry_audit.receivers  # noqa: F401
