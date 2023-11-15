from django.shortcuts import HttpResponse, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
    return HttpResponse('Hi')

@login_required
def create_challenge(request):
    if request.user.groups.filter(name='Company').exists():
        # Render the form/template for creating challenges
        return render(request, 'new_challenge.html')

    return HttpResponseForbidden("Permission Denied")