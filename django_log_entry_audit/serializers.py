from rest_framework import serializers

from django_log_entry_audit.models import LogEntry


class LogEntrySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.status.name

    class Meta:
        model = LogEntry
        fields = ("created", "fields", "user", "status")
