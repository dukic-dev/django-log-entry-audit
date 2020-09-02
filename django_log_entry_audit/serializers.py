from importlib import import_module

from rest_framework import serializers

from django_log_entry_audit.models import LogEntry
from django_log_entry_audit.settings import USER_SERIALIZER


module = import_module(".".join(USER_SERIALIZER.split(".")[:-1]))
UserSerializer = getattr(module, USER_SERIALIZER.split(".")[-1])


class LogEntrySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_status(self, obj):
        return obj.status.name

    class Meta:
        model = LogEntry
        fields = ("created", "fields", "user", "status")
