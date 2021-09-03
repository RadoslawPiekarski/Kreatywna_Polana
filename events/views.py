from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "events/index.html")

def events(request):

    return render((request, "events/all_events.html"))

def event(request, slug):

    return render(request, "events/event.html")
