from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import MeetupPass
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def index(request):
  return redirect('home')

def meetup_pass(request):
  return render(request, 'event_pass/download.html')

def download(request):
  if request.method == 'POST':
    email = request.POST['email']
    try:
      meetup_pass = MeetupPass.objects.get(email=email)
      if meetup_pass.count > 5:
        messages.error(request, 'You have exceeded your download limit.')
        return render(request, 'event_pass/download.html')
      else:
        image = meetup_pass.pass_image.path
        meetup_pass.count += 1
        meetup_pass.save()
        response = FileResponse(open(image, 'rb'))
        return response
    except ObjectDoesNotExist:
      return redirect('error')
  else:
    return redirect('home')

def cancel(request):
  if request.method == 'POST':
    email = request.POST['email']
    try:
      meetup = MeetupPass.objects.get(email=email)
      meetup.is_coming = False
      meetup.save()
      messages.success(request, 'Your Event Registration has been cancelled')
      return render(request, 'event_pass/cancel.html')
    except ObjectDoesNotExist:
      return redirect('error')
  else:
    return render(request, 'event_pass/cancel.html')

def error(request):
  return render(request, 'event_pass/error.html')