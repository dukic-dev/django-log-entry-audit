import datetime
import decimal
import json
import uuid

from django.conf import settings
from django.db import models
from django.utils.duration import duration_iso_string
from django.utils.functional import Promise
from django.utils.timezone import is_aware


DATE_FORMAT = settings.DATE_INPUT_FORMATS[0]
TIME_FORMAT = settings.TIME_INPUT_FORMATS[0]
DATETIME_FORMAT = settings.DATETIME_INPUT_FORMATS[0]


def to_datetime_format(dt):
    return dt.strftime(DATETIME_FORMAT)


def to_date_format(dt):
    return dt.strftime(DATE_FORMAT)


def to_time_format(dt):
    return dt.strftime(TIME_FORMAT)


class ModelEncoder(json.JSONEncoder):
    def default(self, o):
        fields = {}

        for f in o._meta.fields:
            val = getattr(o, f.name)
            if isinstance(f, models.ForeignKey) or isinstance(f, models.OneToOneField):
                fields[f.name] = {
                    "id": val.id if val else "",
                    "name": str(val) if val else ""
                }
            elif isinstance(f, models.FileField):
                fields[f.name] = val.name
            else:
                if isinstance(val, datetime.datetime):
                    fields[f.name] = to_datetime_format(val)
                elif isinstance(val, datetime.date):
                    fields[f.name] = to_date_format(val)
                elif isinstance(val, datetime.time):
                    if is_aware(val):
                        raise ValueError("JSON can't represent timezone-aware times.")
                    fields[f.name] = to_time_format(val)
                elif isinstance(val, datetime.timedelta):
                    fields[f.name] = duration_iso_string(val)
                elif isinstance(val, (decimal.Decimal, uuid.UUID, Promise)):
                    fields[f.name] = str(val)
                else:
                    fields[f.name] = str(val)

        for f in o._meta.many_to_many:
            fields[f.name] = []
            qs = getattr(o, f.name).all()
            for obj in qs:
                fields[f.name].append({
                    "id": obj.id,
                    "name": str(obj)
                })

        return fields
