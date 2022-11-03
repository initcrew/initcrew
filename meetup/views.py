from django.shortcuts import render
from main.models import Team

# Create your views here.
def meetup_team(request):
  team = Team.objects.all().order_by('id')

  context = {
    'team': team
  }
  return render(request, 'meetup/meetup_team.html', context)