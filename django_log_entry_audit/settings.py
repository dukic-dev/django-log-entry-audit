import os

from django.conf import settings


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DEFAULT_AUDIT_SIGNALS = {}

AUDIT_SIGNALS = getattr(settings, "LOG_ENTRY_AUDIT_SIGNALS", DEFAULT_AUDIT_SIGNALS)
USER_SERIALIZER = getattr(settings, "LOG_ENTRY_USER_SERIALIZER")
