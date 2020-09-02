from importlib import import_module

from rest_framework import serializers

from django_log_entry_audit.models import LogEntry
from django_log_entry_audit.settings import USER_SERIALIZER


def import_class(path):
    components = path.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


UserSerializer = import_class(USER_SERIALIZER)


class LogEntrySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_status(self, obj):
        return obj.status.name

    class Meta:
        model = LogEntry
        fields = ("created", "fields", "user", "status")
