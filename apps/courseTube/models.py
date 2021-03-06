from __future__ import unicode_literals
from allauth.account.signals import user_signed_up
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models import *

# Create your models here.


class Tag(Model):
	name = CharField(max_length=10)
	def __unicode__(self):
		return self.name
class Facility(Model):
	image = CharField(max_length=10)
	name = CharField(max_length=10)
	def __unicode__(self):
		return self.name
class WeekDays(Model):
	name = CharField(max_length=10)
	note = CharField(max_length=10, blank=True, null=True)
	def __unicode__(self):
		return self.name

class Student(Model):
	user = OneToOneField(User, related_name="studentProfile")
	tag1 = IntegerField(default = 0)
	tag2 = IntegerField(default = 0)
	tag3 = IntegerField(default = 0)
	tag4 = IntegerField(default = 0)
	tag5 = IntegerField(default = 0)
	tag6 = IntegerField(default = 0)
	tag7 = IntegerField(default = 0)
	tag8 = IntegerField(default = 0)
	tag9 = IntegerField(default = 0)
	tag10 = IntegerField(default = 0)
	tag11 = IntegerField(default = 0)
	tag12 = IntegerField(default = 0)
	tag13 = IntegerField(default = 0)
	tag14 = IntegerField(default = 0)
	tag15 = IntegerField(default = 0)
	tag16 = IntegerField(default = 0)
	def __unicode__(self):
		return self.user.first_name

class InstituteProfile(Model):
	user = OneToOneField(User, related_name="instituteProfile")
	approved = BooleanField(default = False)
	def __unicode__(self):
		return self.user.first_name

class Institute(Model):
	registeredBy = ForeignKey(InstituteProfile, blank=True, null=True)
	listed = BooleanField(default = False)
	deleted = BooleanField(default = False)
	name = CharField(max_length=100, blank=True, null=True)
	logo = CharField(max_length=100, default="http://cometoart.com/wp-content/uploads/2016/03/pojo-placeholder-2.png")
	instituteUrl = CharField(max_length=100, blank=True, null=True)
	description = TextField(blank=True, null=True)
	email = EmailField(blank=True, null=True)
	phone = CharField(max_length=100, blank=True, null=True)
	address = TextField()
	city = CharField(max_length=100)
	pincode = IntegerField()
	state = CharField(max_length=100)
	country = CharField(max_length=100)
	mapLocation = CharField(max_length=100)
	tags = ManyToManyField(Tag, related_name="tags" )
	facility = ManyToManyField(Facility, blank=True)
	weekdays = ManyToManyField(WeekDays, related_name="weekdays")
	startHour = IntegerField()
	endHour = IntegerField()
	establishedSince = IntegerField()
	totalNumberStudents = IntegerField()
	totalNumberFaculty = IntegerField()
	rating = FloatField(default = 0)
	category = CharField(max_length=100, blank=True, null=True)


class Faculty(Model):
	name = CharField(max_length=100)
	details = CharField(max_length=100, blank=True, null=True)
	email = CharField(max_length=100, blank=True, null=True)
	linkedin = CharField(max_length=100, blank=True, null=True)
	webpage = CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return self.name

class Course(Model):
	name = CharField(max_length=100)
	tags = ManyToManyField(Tag, related_name = "courses")
	faculty = ManyToManyField(Faculty, blank=True)
	institute = ForeignKey(Institute, blank=True, null=True, related_name="coursesInstitute")
	students = ManyToManyField(Student, blank=True)
	def __unicode__(self):
		return self.name


class Enroll(Model):
	student = ForeignKey(Student)
	course = ForeignKey(Course)
	institute = ForeignKey(Institute)
	note = CharField(max_length=100, null=True, blank=True)
	def __unicode__(self):
		return str(self.id)

class Review(Model):
	student = ForeignKey(Student)
	when = DateTimeField(default=timezone.now)
	institute = ForeignKey(Institute, related_name="reviews")
	infrastructure = IntegerField(blank=True, null=True) #On a scale of 1-5
	qualityOfEducation = IntegerField(blank=True, null=True) #On a scale of 1-5
	workLoad = IntegerField(blank=True, null=True) #number of hours per week
	feesWorth = IntegerField(blank=True, null=True) #On a scale of 1-5
	postCourseBenifits = IntegerField(blank=True, null=True) #On a scale of 1-5
	postCourseBenifitsText = CharField(max_length=100, blank=True, null=True) 
	recommendedFurther = BooleanField(default = False) #do you want to recommend this course to your friends
	description = TextField(blank=True, null=True)
	userUpVotes = ManyToManyField(Student, blank=True, related_name='likes')
	userDownVotes = ManyToManyField(Student, blank=True, related_name='dislike')


class ReviewRequest(Model):
	approved = BooleanField(default = False) #once approved it get's deleted
	student = ForeignKey(Student)
	institute = ForeignKey(Institute)
	infrastructure = IntegerField() #On a scale of 1-5
	qualityOfEducation = IntegerField() #On a scale of 1-5
	workLoad = IntegerField() #number of hours per week
	feesWorth = IntegerField() #On a scale of 1-5
	postCourseBenifits = IntegerField() #On a scale of 1-5
	postCourseBenifitsText = CharField(max_length=100, blank=True, null=True) 
	recommendedFurther = BooleanField(default = False) #do you want to recommend this course to your friends
	description = TextField(blank=True, null=True)




