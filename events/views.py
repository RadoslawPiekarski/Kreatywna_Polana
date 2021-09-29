from django.shortcuts import render, get_object_or_404
from .models import Event
from django.http import HttpResponseRedirect
from .forms import LoginForm, CreateUserForm

# Create your views here.


def index(request):
    latest_events = Event.objects.all().order_by("-date")[:8]
    return render(request, "events/index.html", {"events": latest_events})


def events(request):
    all_events = Event.objects.all().order_by("-date")
    return render(request, "events/all_events.html", {
        "all_events": all_events
    })

# single event page


def event_detail(request, slug):
    identified_event = get_object_or_404(Event, slug=slug)
    return render(request, "events/event_detail.html", {
        "event": identified_event,
        "instructors": identified_event.instructor.all()
    })


def login(request):
    form = LoginForm()
    # if Post method validate data; if ok redirect to all_events page
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/events/")

    # if GET create and render form
    return render(request, "events/login_form.html", {
        "form": form
    })


def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/events/")

    return render(request, "events/create_user.html", {
        "form": form
    })
