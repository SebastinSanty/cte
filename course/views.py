from django.shortcuts import render
from .models import Course

# Create your views here.

def Courses(request):
	u = Course.objects.all()
	context = {
		"u" : u,
	}
	return render(request, "courses.html", context)
	
