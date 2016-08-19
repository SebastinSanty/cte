from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import os

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
	desc = models.CharField(max_length = 300)
	code = models.CharField(max_length = 10)
	handout = models.FileField(upload_to = "adminuploads/courses/handouts/" , blank=False)
	image = models.ImageField(upload_to = "adminuploads/courses/images/" , blank=True, null=True)
	category = models.CharField(max_length = 50, choices = COURSE_TYPES)
	subcategory = models.CharField(max_length = 50, default = '')
	slack = models.URLField()

	def __str__(self):
		return self.title

class Mentors(models.Model):
	course = models.ForeignKey(Course, related_name = "mentorcourse", on_delete = models.CASCADE)
	mentor = models.ForeignKey(User, related_name = "coursementor", on_delete = models.CASCADE)

	def __str__(self):
		return (self.course.title + " | " + self.mentor.profile.full_name)

class Students(models.Model):
	course = models.ForeignKey(Course, related_name = "studentcourse", on_delete = models.CASCADE)
	student = models.ForeignKey(User, related_name = "coursestudent", on_delete = models.CASCADE)

	def __str__(self):
		return (self.course.title + " | " + self.student.profile.full_name)

class Module(models.Model):
	course = models.ForeignKey(Course, related_name = "modulecourse", on_delete = models.CASCADE)
	number = models.IntegerField()
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150)
	instr = HTMLField()
	upload = models.FileField(upload_to = "adminuploads/courses/uploads/" , blank=True, null=True)

	def __str__(self):
		return self.title

	def typeimg(self):
		name, extension = os.path.splitext(self.upload.name)
		if extension == '.pdf':
			return 'file-pdf-o'
		if extension == '.zip':
			return 'file-archive-o'
		return 'file-o'

	def filename(self):
		return os.path.basename(self.upload.name)
	