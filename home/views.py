from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):
	return render(request,"home.html")

@login_required
def dashboard(request):
	return render(request,"dashboard.html")

@login_required
def profile(request):
	u = Profile.objects.get(user = request.user)
	context = {
		'u':u,
	}
	return render(request, "profile.html")


