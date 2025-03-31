from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm
from .models import Sermon
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .models import Event
from .forms import EventForm
# views.py in church app
from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
from django.http import JsonResponse
from django.conf import settings
from .models import WelcomeContent

def welcome_data(request):
    content = WelcomeContent.objects.all().order_by('-created_at')[:5]  # Get latest 5
    data = [
        {
            'image': request.build_absolute_uri(content.image.url) if content.image else None,
            'verse': content.verse
        }
        for content in content
    ]
    return JsonResponse({'welcome_data': data})





def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')  # Redirect to the event list page
    else:
        form = EventForm()
    return render(request, 'church/events.html', {'form': form})

def event_update(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')  # Redirect to the event list page
    else:
        form = EventForm(instance=event)
    return render(request, 'church/events.html', {'form': form})


# Sermons View
def sermons(request):
    sermons = Sermon.objects.all()
    return render(request, 'church/sermons.html', {'sermons': sermons})

# User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'church/register.html', {'form': form})

# User Login
class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse("member_dashboard")

# User Logout
def logout_view(request):
    logout(request)
    return redirect('/')

# Member Dashboard
@login_required
def member_dashboard(request):
    return render(request, "church/member_dashboard.html")

# Home View
def home(request):
    return render(request, 'church/home.html')

# Ministries View
def ministries(request):
    return render(request, 'church/ministries.html')

# Events View
# views.py in the church app
from django.shortcuts import render

def events(request):
    return render(request, 'church/events.html')  # Adjust as per your template

def give_view(request):
    return render(request, 'church/give.html')