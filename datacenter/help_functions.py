import time
import django


def get_duration(visit):
    time_now = django.utils.timezone.localtime()
    if visit.leaved_at:
        time_delta = visit.leaved_at - visit.entered_at
    else:
        time_delta = time_now - visit.entered_at
    seconds = time_delta.total_seconds()
    return seconds


def format_duration(seconds):
    time_conv = time.gmtime(seconds)
    time_view = time.strftime("%H:%M:%S", time_conv)
    return time_view


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    duration_in_minutes = duration//60
    return duration_in_minutes >= minutes
