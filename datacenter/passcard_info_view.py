from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404, render
from datacenter.help_functions import (get_duration,
                                       format_duration,
                                       is_visit_long)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        seconds = get_duration(visit)
        duration = format_duration(seconds)
        is_suspicious = is_visit_long(visit, minutes=60)
        this_passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_suspicious
            }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
