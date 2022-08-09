from datacenter.models import Visit
from django.shortcuts import render
from datacenter.help_functions import (get_duration,
                                       format_duration,
                                       is_visit_long)


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        seconds = get_duration(visit)
        duration = format_duration(seconds)
        is_suspicious = is_visit_long(visit, minutes=60)
        non_closed_visit = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_suspicious
            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
