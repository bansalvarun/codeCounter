from django.shortcuts import render, redirect, render_to_response, get_object_or_404

from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from models import *

# Create your views here.

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
			registeredBy = Student.objects.get(user = request.user),
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