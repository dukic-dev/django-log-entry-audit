from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _

from enumfields import EnumField
from enum import Enum

from django_log_entry_audit.encoders import JSONEncoder


class StatusEnum(Enum):
    SAVED = "S"
    DELETED = "D"


class LogEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    object_id = models.PositiveIntegerField()
    app_label = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)

    fields = JSONField(encoder=JSONEncoder)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="log_entries",
    )
    status = EnumField(StatusEnum, max_length=1)

    @classmethod
    def get_log_entries_for_object(cls, obj):
        return LogEntry.objects.filter(
            object_id=obj.id, app_label=obj._meta.app_label, model_name=obj._meta.model_name
        ).order_by("created").select_related("user")

    def __str__(self):
        return f"Log Entry for {self.app_label}.{self.model_name} - pk: {self.object_id}"

    class Meta:
        verbose_name = _("Log Entry")
        verbose_name_plural = _("Log Entries")
