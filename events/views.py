from django.shortcuts import render
from datetime import date, time
from .models import Event

# Create your views here.

# mocking data:
all_events = [
    {
        "slug": "kreatywne-zabawy",
        "image": "zajecia_sensoryczne.jpg",
        "host": "Monika",
        "date": date(2021, 8, 29),
        "time": time(14, 00),
        "place": "Olszak",
        "group": "Misie",
        "title": "Kreatywne Zabawy",
        "excerpt": "Tu jest zajawka. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Tu jest content. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi.",
        "is_active": True,
    },
    {
        "slug": "tor-przeszkod",
        "image": "zajecia_sensoryczne_2.jpg",
        "host": "Radek",
        "date": date(2023, 8, 31),
        "time": time(16, 30),
        "place": "Osiedle Przemysława",
        "group": "Skrzaty",
        "title": "Tor przeszkód",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi.",
        "is_active": True,
    },
    {
        "slug": "zapach_jesieni",
        "image": "zapach_jesieni.jpg",
        "host": "Monika",
        "date": date(2021, 8, 29),
        "time": time(11, 00),
        "place": "Olszak",
        "group": "Skrzaty",
        "title": "Zapach jesieni",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi.",
        "is_active": True,
    },
]


def get_date(event):
    return event['date']


def index(request):
    latest_events = Event.objects.all().order_by("-date")[:8]
    # sorted_events = sorted(all_events, key=get_date)
    # latest_events = sorted_events[-3:]
    return render(request, "events/index.html", {"events": latest_events})


def events(request):
    all_events = Event.objects.all().order_by("-date")
    return render(request, "events/all_events.html", {"all_events": all_events})

# single event page


def event_detail(request, slug):
    identfied_event = next(event for event in all_events if event['slug'] == slug)
    return render(request, "events/event_detail.html", {"event": identfied_event})
