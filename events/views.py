from django.shortcuts import render, get_object_or_404
from datetime import date, time
from .models import Event

# Create your views here.


def index(request):
    latest_events = Event.objects.all().order_by("-date")[:8]
    # sorted_events = sorted(all_events, key=get_date)
    # latest_events = sorted_events[-3:]
    return render(request, "events/index.html", {"events": latest_events})


def events(request):
    all_events = Event.objects.all().order_by("-date")
    return render(request, "events/all_events.html", {
        "all_events": all_events
    })

# single event page


def event_detail(request, slug):
    identified_event = get_object_or_404(Event, slug=slug)
    # identified_event = next(event for event in all_events if event['slug'] == slug)
    return render(request, "events/event_detail.html", {
        "event": identified_event,
        "instructors": identified_event.instructor.all()
    })


def login(request):
    return render(request, "events/login_form.html")
