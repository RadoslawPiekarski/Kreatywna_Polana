from django.shortcuts import render, get_object_or_404
from .models import Event, UserProfile, Kid
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import LoginForm, CreateUserForm
from django.views import View
from django.views.generic import ListView


# Create your views here.


def index(request):
    """Main page view. Passing last new 8 events to the template."""
    latest_events = Event.objects.order_by("-date")[:8]
    return render(request, "events/index.html", {"events": latest_events})


class Events(ListView):
    """Generating page showing all events, ordered by newest. Passing all events data."""
    template_name = "events/all_events.html"
    model = Event
    context_object_name = "all_events"

#  function (old) version of Events view
# def events(request):
#     """Generating page showing all events, ordered by newest. Passing all events data."""
#     all_events = Event.objects.all().order_by("-date")
#     return render(request, "events/all_events.html", {
#         "all_events": all_events
#     })


# single event page
def event_detail(request, slug):
    """Generating single event page. Page allows to sign up for event for user or user kids.
    Passing given event data, event instructors and logged user kids."""
    identified_event = get_object_or_404(Event, slug=slug)
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, "events/event_detail.html", {
            "event": identified_event,
            "instructors": identified_event.instructor.all(),
            "kids": Kid.objects.filter(parent=current_user)
        })

    else:
        return render(request, "events/event_detail.html", {
            "event": identified_event,
            "instructors": identified_event.instructor.all(),

        })


class Login(View):
    """Login page. If GET method, generate a form; if POST method, take data form the form, validate and
    save them to the database"""

    def get(self, request):
        form = LoginForm()
        return render(request, "events/login_form.html", {
            "form": form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # TODO Add login and password checkin
            # TODO link login user if validated
            # form.save()
            return HttpResponseRedirect("/events/")


class CreateUser(View):
    """Create new user page. Generate form, validate and save the new user data to database"""

    def get(self, request):
        form = CreateUserForm()
        return render(request, "events/create_user.html", {
            "form": form
        })

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["firstname"],
                last_name=form.cleaned_data["lastname"],
                email=form.cleaned_data["email"],
            )
            user.save()

            user_profile = UserProfile(
                phone_number=form.cleaned_data['phone_number'],
                user=user
            )
            user_profile.save()

            kid = Kid(
                kid_name=form.cleaned_data["kid_name"],
                birth_date=form.cleaned_data["birth_date"],
                parent=user
            )
            kid.save()

            return HttpResponseRedirect("/events/")


# Proof on concept page for logged in users
def parents_info_page(request):
    if request.user.is_authenticated:
        return render(request, "events/parents_info.html")
    else:
        return HttpResponseRedirect("")
