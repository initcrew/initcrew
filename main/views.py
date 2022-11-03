from django.shortcuts import render
from .models import Event, Project, Team

# Create your views here.
def home(request): 
  upcoming_events =  Event.objects.filter(is_upcoming=True).order_by('id')
  past_events = Event.objects.filter(is_upcoming=False).order_by('-id')

  context = {
    'upcoming_events': upcoming_events,
    'past_events': past_events
  }
  return render(request, 'main/home.html', context)

def team(request):
  founders = Team.objects.filter(is_admin=True)

  context = {
    'founders': founders,
  }
  return render(request, 'main/our_team.html', context)

def contact(request):
  return render(request, 'main/contact.html')

def projects(request):
  projects = Project.objects.all()
  context = {
    'projects': projects
  }
  return render(request, 'main/projects.html', context)