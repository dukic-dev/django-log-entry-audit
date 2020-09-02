from json import loads

from django.conf import settings
from django.core import serializers
from django.dispatch import receiver

from django_log_entry_audit.models import LogEntry, StatusEnum
from django_log_entry_audit.settings import AUDIT_SIGNALS


def _get_object_serialized_fields(obj):
    return loads(serializers.serialize("json", [obj]))[0]["fields"]


try:

    @receiver(AUDIT_SIGNALS["create"])
    def create_log_entry(sender, **kwargs):
        obj = kwargs["obj"]
        user = kwargs["user"]

        LogEntry.objects.create(
            object_id=obj.pk,
            app_label=obj._meta.app_label,
            model_name=obj._meta.model_name,
            fields=_get_object_serialized_fields(obj),
            user=user,
            status=StatusEnum.SAVED,
        )


except KeyError:
    pass


try:

    @receiver(AUDIT_SIGNALS["update"])
    def update_log_entries(sender, **kwargs):
        objs = kwargs["objs"]
        user = kwargs["user"]

        log_entries = []
        for obj in objs:
            log_entries.append(
                LogEntry(
                    object_id=obj.pk,
                    app_label=obj._meta.app_label,
                    model_name=obj._meta.model_name,
                    fields=_get_object_serialized_fields(obj),
                    user=user,
                    status=StatusEnum.SAVED,
                )
            )

        LogEntry.objects.bulk_create(log_entries)


except KeyError:
    pass


try:

    @receiver(AUDIT_SIGNALS["delete"])
    def delete_log_entry(sender, **kwargs):
        obj = kwargs["obj"]
        user = kwargs["user"]

        LogEntry.objects.create(
            object_id=obj.pk,
            app_label=obj._meta.app_label,
            model_name=obj._meta.model_name,
            fields=_get_object_serialized_fields(obj),
            user=user,
            status=StatusEnum.DELETED,
        )


except KeyError:
    pass


try:

    @receiver(AUDIT_SIGNALS["bulk_create"])
    def create_log_entries(sender, **kwargs):
        objs = kwargs["objs"]
        user = kwargs["user"]

        log_entries = []
        for obj in objs:
            log_entries.append(
                LogEntry(
                    object_id=obj.pk,
                    app_label=obj._meta.app_label,
                    model_name=obj._meta.model_name,
                    fields=_get_object_serialized_fields(obj),
                    user=user,
                    status=StatusEnum.SAVED,
                )
            )

        LogEntry.objects.bulk_create(log_entries)


except KeyError:
    pass


try:

    @receiver(AUDIT_SIGNALS["bulk_delete"])
    def delete_log_entries(sender, **kwargs):
        objs = kwargs["objs"]
        user = kwargs["user"]

        log_entries = []
        for obj in objs:
            log_entries.append(
                LogEntry(
                    object_id=obj.pk,
                    app_label=obj._meta.app_label,
                    model_name=obj._meta.model_name,
                    fields=_get_object_serialized_fields(obj),
                    user=user,
                    status=StatusEnum.DELETED,
                )
            )

        LogEntry.objects.bulk_create(log_entries)


except KeyError:
    pass
