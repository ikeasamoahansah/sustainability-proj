from django.shortcuts import render, HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return HttpResponse('Hi')

@login_required
def create_goal(request):
    if request.user.groups.filter(name='Normal User').exists():
        # Render the form/template for creating goals
        return render(request, 'new_goal.html')

    return HttpResponseForbidden("Permission Denied")


