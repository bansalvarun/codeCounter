from django.shortcuts import render, redirect, render_to_response, get_object_or_404

from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request, 'demo/home.html')

@login_required
def index(request):
	return render(request, 'demo/home.html')
