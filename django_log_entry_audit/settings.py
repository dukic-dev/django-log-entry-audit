import os

from django.conf import settings


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DEFAULT_AUDIT_SIGNALS = {}
DEFAULT_REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%d/%m/%Y %H:%M",
    "DATETIME_INPUT_FORMATS": ["%d/%m/%Y"],
    "DATE_FORMAT": "%d/%m/%Y",
    "DATE_INPUT_FORMATS": ["%d/%m/%Y %H:%M", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y",],
    "TIME_INPUT_FORMATS": ["%H:%M", "%H:%M:%S", "%H:%M:%S.%f",],
}

AUDIT_SIGNALS = getattr(settings, "LOG_ENTRY_AUDIT_SIGNALS", DEFAULT_AUDIT_SIGNALS)
USER_SERIALIZER = getattr(settings, "LOG_ENTRY_USER_SERIALIZER")
REST_FRAMEWORK = getattr(settings, "REST_FRAMEWORK", DEFAULT_REST_FRAMEWORK)
