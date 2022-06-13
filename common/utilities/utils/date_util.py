"""
This module consists of date util
"""
from datetime import datetime, timedelta
from django.utils import timezone
import zoneinfo
import arrow


class DateUtil(object):

    @classmethod
    def getTimeZone(cls):
        return zoneinfo.ZoneInfo('Asia/Kolkata')

    @classmethod
    def getUTCTimeZone(cls):
        return zoneinfo.ZoneInfo('UTC')

    @classmethod
    def getNow(cls):
        return datetime.now()

    @classmethod
    def getTZAwareNow(cls):
        return timezone.make_aware(cls.getNow())

    @classmethod
    def convertTZAware(cls, obj):
        return obj.astimezone(cls.getTimeZone())

    @classmethod
    def getUtcTimeNow(cls):
        return cls.getNow().astimezone(cls.getUTCTimeZone())

    @classmethod
    def getTimeOnly(cls):
        return cls.getNow().time()

    @classmethod
    def getDateOnly(cls):
        return cls.getNow().date()

    @classmethod
    def get_epoch_from_date(cls, date):
        dt = datetime.strptime(date, "%Y-%m-%d").date()
        epoch = cls.getDateOnly().fromtimestamp(0)
        delta = dt - epoch
        # to seconds
        return int(delta.total_seconds())

    @classmethod
    def get_epoch_from_datetime(cls, date_):
        dt = datetime.strptime(date_, "%Y-%m-%d %H:%M:%S")
        epoch = cls.getNow().fromtimestamp(0)
        delta = dt - epoch
        # to seconds
        return int(delta.total_seconds())

    @classmethod
    def get_date_from_epoch(cls, epoch, is_millisec=False):
        if is_millisec:
            epoch = int(epoch) / 1000
        return datetime.fromtimestamp(int(epoch))

    @classmethod
    def addDateOnly(cls, days):
        d = timedelta(days=days)
        currentDateTime = cls.getNow() + d
        return currentDateTime.date()

    @classmethod
    def addDateTime(cls, days):
        d = timedelta(days=days)
        currentDateTime = cls.getNow() + d
        return currentDateTime
