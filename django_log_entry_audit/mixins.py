from rest_framework.decorators import action
from rest_framework.response import Response

from django_log_entry_audit.models import LogEntry
from django_log_entry_audit.serializers import LogEntrySerializer


class HistoryViewSetMixin:
    @action(detail=True, methods=["get"])
    def history(self, request, pk=None):
        instance = self.get_object()
        serializer = LogEntrySerializer(LogEntry.get_log_entries_for_object(instance), many=True)
        return Response(serializer.data)
