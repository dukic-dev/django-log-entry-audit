import datetime
import decimal
import json
import uuid

from django.conf import settings
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


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return to_datetime_format(o)
        elif isinstance(o, datetime.date):
            return to_date_format(o)
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            return to_time_format(o)
        elif isinstance(o, datetime.timedelta):
            return duration_iso_string(o)
        elif isinstance(o, (decimal.Decimal, uuid.UUID, Promise)):
            return str(o)
        else:
            return super().default(o)
