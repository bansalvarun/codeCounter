from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
import json
# from django.core.
import random
# import matplotlib.pyplot as plt
import numpy as np
# from sklearn.manifold import TSNE
# from sklearn import cluster
from sets import Set

from models import *
# Create your views here.


tags = ["computer science","web development","android app","machine learning", 'entrance exam','AIPMT', 'IIT-JEE',"BITSAT", 'consultancy','higher education', 'career', 'test prep', 'upsc', 'general knowledge', 'interview', 'language']

def recommend_cluster(cur_user):
	tags = ["computer science","web development","android app","machine learning", 'entrance exam','AIPMT', 'IIT-JEE',"BITSAT", 'consultancy','higher education', 'career', 'test prep', 'upsc', 'general knowledge', 'interview', 'language']
	students = Student.objects.all()
	num_of_users = len(students)
	print "ahhah"
	num_of_tags = 16
	similar_users = Set([])
	similar_institutes = Set([])
	sqrt_n = int(num_of_tags**0.5) # divide cluster into sqrt n chunks
	for sqrt_comp in xrange(0, num_of_tags, sqrt_n):
		for student in students:
			if(student.id != cur_user.id):
				bits = 0
				user_bits = 0;
				if sqrt_comp == 0:
					bits = int(student.tag1) + int(student.tag2) + int(student.tag3) + int(student.tag4) 
					user_bits = int(cur_user.tag1) + int(cur_user.tag2) + int(cur_user.tag3) + int(cur_user.tag4)
					favorable_tags = [tags[cur_user.tag1+1], tags[cur_user.tag2+1], tags[cur_user.tag3+1], tags[cur_user.tag4+1]]
					if bits == user_bits:
						for i in favorable_tags:
							tag = Tag.objects.get(name = i)
							print tag
							c = tag.tags.all()
							print c
							for j in c:
								similar_institutes.add(j)
				elif sqrt_comp == 1:
					bits = int(student.tag5) + int(student.tag6) + int(student.tag7) + int(student.tag8) 
					user_bits = int(cur_user.tag5) + int(cur_user.tag6) + int(cur_user.tag7) + int(cur_user.tag8)
					favorable_tags = [tags[cur_user.tag5-1], tags[cur_user.tag6-1], tags[cur_user.tag7-1], tags[cur_user.tag8-1]]
					if bits == user_bits:
						for i in favorable_tags:
							tag = Tag.objects.get(name = i)
							c = tag.tags.all()
							print c
							for j in c:
								similar_institutes.add(j)

				elif sqrt_comp == 2:
					bits = int(student.tag9) + int(student.tag10) + int(student.tag11) + int(student.tag12) 
					user_bits = int(cur_user.tag9) + int(cur_user.tag10) + int(cur_user.tag11) + int(cur_user.tag12)
					favorable_tags = [tags[cur_user.tag9-1], tags[cur_user.tag10-1], tags[cur_user.tag11-1], tags[cur_user.tag12-1]]
					if bits == user_bits:
						for i in favorable_tags:
							tag = Tag.objects.get(name = i)
							c = tag.tags.all()
							print c
							for j in c:
								similar_institutes.add(j)

				elif sqrt_comp == 3:
					bits = int(student.tag13) + int(student.tag14) + int(student.tag15) + int(student.tag16) 
					user_bits = int(cur_user.tag13) + int(cur_user.tag14) + int(cur_user.tag15) + int(cur_user.tag16)
					favorable_tags = [tags[cur_user.tag13-1], tags[cur_user.tag14-1], tags[cur_user.tag15-1], tags[cur_user.tag16-1]]
					if bits == user_bits:
						for i in favorable_tags:
							tag = Tag.objects.get(name = i)
							c = tag.tags.all()
							print c
							for j in c:
								similar_institutes.add(j)

	print cur_user.id, "cur_user.id"
	print similar_institutes
	return similar_institutes


# def plot_cluster(point_label, adj_users_tag):
# 	model = TSNE(learning_rate = 200.0)
# 	tsne_data = model.fit_transform(adj_users_tag)

# 	print "Points labels : " + str(point_label)
# 	plt.scatter(tsne_data[:,0], tsne_data[:,1], c = point_label)
# 	plt.title("Clutser")
# 	plt.show()


def home(request):
	args = {}
	try:
		student = Student.objects.get(user = request.user)
		institutes = list(recommend_cluster(student))[:10]
	except:
		institutes = Institute.objects.order_by('-rating')
	trendings = Institute.objects.order_by('-rating')[:10]
	tags = Tag.objects.all()
	args["institutes"] = institutes
	args["tags"] = tags
	args["trendings"] = trendings
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
	return redirect("/")


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

	return redirect("/")


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
	return render(request, 'courseTube/institutes.html', args) 

def institute(request, id):
	args = {}
	args.update(csrf(request))
	institute = Institute.objects.get(pk=id)
	args["institute"] = institute
	print institute.tags.all()
	try:
		print request.user.id
		student = Student.objects.get(user = request.user)
		for i in institute.tags.all():
			x = tags.index(i.name) + 1
			if(x==1):
				student.tag1 = 1
			elif(x==2):	
				student.tag2 = 1
			elif(x==3):	
				student.tag3 = 1
			elif(x==4):	
				student.tag4 = 1
			elif(x==5):	
				student.tag5 = 1
			elif(x==6):	
				student.tag6 = 1
			elif(x==7):	
				student.tag7 = 1
			elif(x==8):	
				student.tag8 = 1
			elif(x==9):	
				student.tag9 = 1
			elif(x==10):	
				student.tag10 = 1
			elif(x==11):	
				student.tag11 = 1
			elif(x==12):	
				student.tag12 = 1
			elif(x==13):	
				student.tag13 = 1
			elif(x==14):	
				student.tag14 = 1
			elif(x==15):	
				student.tag15 = 1
			elif(x==16):	
				student.tag16 = 1
			student.save()
	except:
		print "No user logged in"
	return render(request, 'courseTube/institute.html', args)

def category(request, categoryId):
	args = {}
	institutes = Institute.objects.all()
	args["institutes"] = institutes
	return render(request, 'courseTube/category.html', args) 

def tag(request, tagId):
	args = {}
	tag = tag.objects.get(pk=tagId)
	args["tag"] = tag
	return render(request, 'courseTube/tag.html', args) 

def tags(request):
	args = {}
	tags = Tag.objects.all()
	args["tags"] = institutes
	return render(request, 'courseTube/tags.html', args) 

def compare(request):
	args = {}
	institutes = Institute.objects.all()
	args["institutes"] = institutes
	args["insti"] = []
	args["rating"] = []
	for i in institutes:
		print i
		args["insti"].append(i.name)
		args["rating"].append(i.rating)
	args["insti"] = json.dumps(args["insti"] )
	return render(request, 'courseTube/compare.html', args)
swearWords = ['anal','anus','arse','ass','ballsack','balls','bastard','bitch','biatch','bloody','blowjob','blow job','bollock','bollok','boner','boob',"bugger","bum","butt","buttplug","clitoris","cock",'coon','crap','cunt',"damn",'dick','dildo','dyke','fag','feck','fellate','fellatio','felching','fuck','f u c k','fudgepacker','fudge', 'packer','flange','Goddamn','God' 'damn','hell','homo','jerk','jizz','knobend','knob end','labia','lmao','lmfao','muff','nigger','nigga','omg','penis','piss','poop','prick','pube','pussy','queer','scrotum',"sex",'shit','shit','sh1t','slut','smegma','spunk','tit','tosser','turd',"twat","vagina","wank","whore","wtf"]

@login_required
def postFeedback(request):
	student = get_object_or_404(Student, user = request.user)
	if request.method == "POST":
		institute = get_object_or_404(Institute, pk=request.POST["instituteId"])
		for i in swearWords:
			if i in request.POST["description"]:
				return HttpResponse("You are not allowed to use swear words!")
		review = Review(
			student = student,
			institute = institute, 
			description = request.POST["description"],
			qualityOfEducation = request.POST["qualityOfEducation"]
			)
		review.save()
		getRatingInsti()
		return redirect("/institute/"+request.POST["instituteId"])

def getRatingInsti():
	insti = Institute.objects.all()
	for i in insti:
		allReviews = i.reviews.all()
		mysum = 0
		for j in allReviews:
			mysum += j.qualityOfEducation
		print mysum, 
		print len(allReviews),
		i.rating = mysum/float(len(allReviews))
		i.rating = ("%.2f" % i.rating)
		print i.rating
		i.save()
def locationsOfInstitues(request):
	args = {}
	institutes = Institute.objects.all()
	args["institutes"] = institutes
	return render(request, "courseTube/locationsOfInstitutes.html", args)



def createRandomReviews(request):
	review = Review.objects.all()
	for i in review:
		i.delete()
	students = Student.objects.all()
	institutes = Institute.objects.all()
	for student in students:
		p = random.randrange(1,100)
		for institute in institutes:
			if(p%5):
				review = Review(
					student = student,
					institute = institute, 
					description = "This is a sample comment for sample data!",
					qualityOfEducation = random.randrange(1,5,1)
					)
				review.save()
	print "reviews done" 
	getRatingInsti()
	return HttpResponse("ok")


def fixStudentsName(request):
	x = "shivani isha smt shyani devi divya mansi mazida pooja kajal meena sonam buity hina shakshi sagar pooja anita neetu anshu d/o kanika kathuria manju shakshi anita reena neha khushboo aasmin jyoti riya masi rekha leela with a child isha gulshan priya jain pooja rakhi @payal versha sunita nitu kumari vandana roshni parveen versa kavita pooja sarojani nagina tapas das priyanka santna khushbu pooja any bobby deeya kumari anjali juneja anjali @ babli champa karketta anshu monika rimmi singh aanamika misra chahat manju nagma khatoon pooja sonam koshal laxmi devi w/o late sh hukan chand sandhya poonam sna nikita senger layba noor iqra salima naziya siddiqui priti kamni sandhya renu @ rinki priya pooja minakchi ruby smt.farhana baigum sheetal kalyani patro anjali priyanka palak @ simran babita gurdeep kaur dhanwanti devi fooljhnah vandana smt. gyatri devi shehnaz kajal pooja ranju barjraj ramdin verma sharat chandran birender mandal amit kushal kasid shiv prakash vikram singh sanjay abhi ram dutt gupta khadak singh gurmit singh chanderpal aman khursid rajeev durgesh nahar singh ram kumar sunder paal maansingh aswal rohit rohit sparsh santosh santosh punit khandelwal dinesh gulshan arvind kumar yadav nausad gurmit singh md. afsar shiv shakti singh moti lal kausal kumar rohit rohit mohabbat ali raj kumar jaswant singh sevak @ pitambar lal chotelal amit rupesh midda dharam singh manoj yadav @ manoj ram singh preetam kumar ram kumar sarain pankaj kumar sheak shakir riyasat ali vinit katariya sumit arindra kali charan badshya khan vikash devinder chadda aman mohan singh hemant shivam yash mittal aakash chandesh sumit mitra supriyal sen gajender singh @ goldy pooran chand sharma irfan azaruddin mukul yadav pooran chand sharma manoj sanjay charee raja babu pawan sandeep rajkumar chawla parvesh mohd ataullah neeraj kumar jamil khan yogita rijul aggarwal mohd shakib rahul kumar rajender suraj rizwan sandeep md mustafa har parsad deepak vidhi"
	x = x.split()
	print x
	students = Student.objects.all()
	i = 0
	for student in students:
		while(i!= "" or i != "@"):
			i+=1
			if(i>=len(x)):
				break
		if(i>=len(x)):
			break
		student.name = x[i]
		i+=1

	return HttpResponse("ok")


def populateDatabaseRandom():
	# if(len(Tag.objects.all())<2):
	# 	for _tag in tags:
	# 		tag = Tag(name = _tag)
	# 		tag.save()
	# print "tags done"
	tags = Tag.objects.all()
	# if(len(Student.objects.all())<20):
	# 	x = "shivani isha smt shyani devi divya mansi mazida pooja kajal meena sonam buity hina shakshi sagar pooja anita neetu anshu d/o kanika kathuria manju shakshi anita reena neha khushboo aasmin jyoti riya masi rekha leela with a child isha gulshan priya jain pooja rakhi @payal versha sunita nitu kumari vandana roshni parveen versa kavita pooja sarojani nagina tapas das priyanka santna khushbu pooja any bobby deeya kumari anjali juneja anjali @ babli champa karketta anshu monika rimmi singh aanamika misra chahat manju nagma khatoon pooja sonam koshal laxmi devi w/o late sh hukan chand sandhya poonam sna nikita senger layba noor iqra salima naziya siddiqui priti kamni sandhya renu @ rinki priya pooja minakchi ruby smt.farhana baigum sheetal kalyani patro anjali priyanka palak @ simran babita gurdeep kaur dhanwanti devi fooljhnah vandana smt. gyatri devi shehnaz kajal pooja ranju barjraj ramdin verma sharat chandran birender mandal amit kushal kasid shiv prakash vikram singh sanjay abhi ram dutt gupta khadak singh gurmit singh chanderpal aman khursid rajeev durgesh nahar singh ram kumar sunder paal maansingh aswal rohit rohit sparsh santosh santosh punit khandelwal dinesh gulshan arvind kumar yadav nausad gurmit singh md. afsar shiv shakti singh moti lal kausal kumar rohit rohit mohabbat ali raj kumar jaswant singh sevak @ pitambar lal chotelal amit rupesh midda dharam singh manoj yadav @ manoj ram singh preetam kumar ram kumar sarain pankaj kumar sheak shakir riyasat ali vinit katariya sumit arindra kali charan badshya khan vikash devinder chadda aman mohan singh hemant shivam yash mittal aakash chandesh sumit mitra supriyal sen gajender singh @ goldy pooran chand sharma irfan azaruddin mukul yadav pooran chand sharma manoj sanjay charee raja babu pawan sandeep rajkumar chawla parvesh mohd ataullah neeraj kumar jamil khan yogita rijul aggarwal mohd shakib rahul kumar rajender suraj rizwan sandeep md mustafa har parsad deepak vidhi"
	# 	file = x.split()
	# 	for i in file:
	# 		print i
	# 		try:
	# 			user = User.objects.get(user = str(i))
	# 		except:
	# 			user=User.objects.create_user(str(i), password=str(i))
	# 			user.is_superuser=False
	# 			user.is_staff=False
	# 			user.save()
	# 			student = Student(user=user)
	# 			student.save()

	# print "students done"
	# if(len(InstituteProfile.objects.all())<20):
	# 	file = "OLIVER JACK HARRY JACOB CHARLIE THOMAS GEORGE OSCAR JAMES WILLIAM NOAH ALFIE JOSHUA MUHAMMAD HENRY LEO ARCHIE ETHAN JOSEPH FREDDIE SAMUEL ALEXANDER LOGAN DANIEL ISAAC MAX MOHAMMED BENJAMIN MASON LUCAS EDWARD HARRISON JAKE DYLAN RILEY FINLEY THEO SEBASTIAN ADAM ZACHARY ARTHUR TOBY JAYDEN LUKE HARLEY LEWIS TYLER HARVEY MATTHEW DAVID REUBEN MICHAEL ELIJAH KIAN "
	# 	# file = open("/staticfiles/media/americanNames.txt", "r")
	# 	file = file.split()
	# 	for i in file:
	# 		try:
	# 			user = User.objects.get(user = str(i))
	# 		except:
	# 			user=User.objects.create_user(str(i), password=str(i))
	# 			user.is_superuser=False
	# 			user.is_staff=False
	# 			user.save()
	# 			instituteProfile = InstituteProfile(user=user)
	# 			instituteProfile.save()

	# print "institute profiles done"
	for i in Institute.objects.all():
		i.delete()
	if( len(Institute.objects.all())<20):
		instituteProfile = InstituteProfile.objects.all()
		for i in instituteProfile:
			institute = Institute(
				registeredBy = i,
				listed = True,
				name = str(i.user) + " Classes",
				instituteUrl  = str(i) + ".com",
				description = "This is dummy data created to make analysis and make results",
				email = str(i)+"@gmail.com",
				phone = "72133" + str(random.randrange(340, 955,1)),
				address = "Some random address",
				city = "Delhi",
				pincode = "1" + str(random.randrange(10000, 12000,1)),
				# tags = [],
				# facility = [],
				# weekdays = [],
				state = "Delhi",
				country = "India",
				mapLocation = "https://www.google.co.in/maps/@28.6327"+str(random.randrange(0,1000,1))+",77.2204"+str(random.randrange(0,1000,1))+",15z?hl=en",
				establishedSince= 1980 + random.randrange(0,30,1),
				totalNumberStudents = '100',
				totalNumberFaculty = '100',
				startHour = 8,
				endHour = 16
				)
			institute.save()
# populateDatabaseRandom()
 
#from apps.courseTube.views import *
			
			for weekday in WeekDays.objects.all():
				if(weekday.id<5):
					institute.weekdays.add(weekday)
			for tag in tags:
				p = random.randrange(0,100,1)
				if(p%2):
					institute.tags.add(tag)
			institute.save()

	print "institutes done"









