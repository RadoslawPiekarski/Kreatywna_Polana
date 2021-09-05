from django.shortcuts import render
from datetime import date, time

# Create your views here.

# mocking data:
all_events = [
    {
        "slug": "kreatywne-zabawy",
        "image": "image1.jpg",
        "host": "Monika",
        "date": date(2021, 8, 29),
        "time": time(14, 00),
        "place": "Olszak",
        "group": "Misie",
        "title": "Kreatywne Zabawy",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi.",
        "is_active": True,
    },
    {
        "slug": "tor-przeszkod",
        "image": "image2.jpg",
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
        "slug": "kreatywne-zabawy",
        "image": "image1.jpg",
        "host": "Monika",
        "date": date(2021, 8, 29),
        "time": time(11, 00),
        "place": "Olszak",
        "group": "Skrzaty",
        "title": "Kreatywne Zabawy",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in.",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nec ligula magna. Praesent aliquet rhoncus massa, blandit rhoncus mauris malesuada in. Sed vulputate, orci id varius rutrum, eros nunc mollis nunc, vitae ornare sem orci sed nisi.",
        "is_active": True,
    },
]


def get_date(event):
    return event['date']


def index(request):
    sorted_events = sorted(all_events, key=get_date)
    latest_events = sorted_events[-3:]
    return render(request, "events/index.html", {"events": latest_events})


def events(request):

    return render(request, "events/all_events.html")

# single event page


def event_detail(request, slug):

    return render(request, "events/event.html")
