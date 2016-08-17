from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def Courses(request):
	u = Course.objects.all()
	context = {
		"u" : u,
	}
	return render(request, "courses.html", context)

def Coursereg(request, pk):
	u = Course.objects.get(code = pk)
	if Students.objects.filter(course = u, student = request.user).count() > 0 :
		reg = True
	else:
		reg = False
	context = {
		"u" : u,
		"reg": reg,
	}
	if request.POST.get("register"):
		print("Hello")
		m = Students(course = u, student = request.user)
		m.save()
		return redirect('courses')
	if request.POST.get("deregister"):
		print("Hello")
		m = Students.objects.filter(course = u, student = request.user).delete()
		return redirect('courses')
	return render(request, "coursereg.html", context)
	
def Coursepage(request, pk):
	u = Course.objects.get(code = pk)
	m = Students.objects.filter(course = u, student = request.user)
	if m.count() > 0 :
		mod = u.modulecourse.all().order_by('number')
		print(mod[0])
		context = {
			'i': u,
			'mod': mod,
		}
		return render(request, "course.html", context)
	else:
		return render(request, "home.html")

