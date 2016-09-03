from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from models import *

# Create your views here.

def home(request):
	args = {}
	institutes = Institute.objects.all()
	args["institutes"] = institutes
	return render(request, 'demo/home.html', args)


@login_required
def registerAsStudent(request):
	print request.user.id
	user = request.user
	try:
		student = Student.objects.get(user = request.user)
		print student
	except:
		student = Student(user = user)
		student.save()
	return render(request, 'demo/home.html')


@login_required
def registerAsInstitute(request):
	args = {}
	user = request.user
	try:
		instituteProfile = InstituteProfile.objects.get(user = request.user)
		print instituteProfile
	except:
		try:
			student = Student.objects.get(user = request.user)
			return HttpResponse("Sorry, You are registered as a Student!")
		except:		
			instituteProfile = InstituteProfile(user = user)
			instituteProfile.save()
	args["user"] = user
	instituteProfile = InstituteProfile(user = user)
	args["instituteProfile"] = instituteProfile

	return render(request, 'demo/home.html')


@login_required
def registerInstitute(request):
	args = {}
	args.update(csrf(request))
	tags = Tag.objects.all()
	facilities = Facility.objects.all()
	weekdays = WeekDays.objects.all()
	args["tags"] = tags
	args["facilities"] = facilities
	args["weekdays"] = weekdays

	return render(request, 'courseTube/registerInstitute.html',args)

def requestInstitute(request):
	if request.method=="POST":
		institute = Institute(
			registeredBy = User.objects.get(user = request.user),
			name = request.POST["name"],
			address = request.POST["address"],
			city = request.POST["city"],
			pincode = request.POST["pincode"],
			state = request.POST["state"],
			country= request.POST["country"],
			mapLocation= request.POST["mapLocation"],
			tags= request.POST["tags"],
			facility= request.POST["facility"],
			weekdays= request.POST["weekdays"],
			startHour= request.POST["startHour"],
			endHour= request.POST["endHour"],
			establishedSince= request.POST["establishedSince"],
			totalNumberStudents = request.POST["totalNumberStudents"],
			totalNumberFaculty  = request.POST["totalNumberFaculty"]
			)
# @login_required
# def institutesRequests(request):
	

def institutes(request):
	args = {}
	institutes = Institute.objects.all()
	args["institutes"] = institutes
	return render(request, 'courseTube/institute.html', args) 