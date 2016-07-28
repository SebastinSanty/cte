from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

COURSE_TYPES = (
	(u'Electronics',u'Electronics'),
	(u'Computer Science',u'Computer Science'),
	(u'Mechanical',u'Mechanical'),
	(u'Chemical',u'Chemical'),
	(u'Graphics and Designing',u'Graphics and Designing'),
	)

# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150)
	code = models.CharField(max_length = 10)
	handout = models.FileField(upload_to = "adminuploads/courses/handouts/" , blank=False)
	image = models.ImageField(upload_to = "adminuploads/courses/images/" , blank=True, null=True)
	category = models.CharField(max_length = 50, choices = COURSE_TYPES)
	subcategory = models.CharField(max_length = 50)

	def __str__(self):
		return self.title

class Mentors(models.Model):
	course = models.ForeignKey(Course, related_name = "mentorcourse", on_delete = models.CASCADE)
	mentor = models.ForeignKey(User, related_name = "mentor", on_delete = models.CASCADE)

	def __str__(self):
		return self.course

class Module(models.Model):
	course = models.ForeignKey(Course, related_name = "modulecourse", on_delete = models.CASCADE)
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150)
	instr = HTMLField()
	upload = models.FileField(upload_to = "adminuploads/courses/uploads/" , blank=True, null=True)

	def __str__(self):
		return self.title
	