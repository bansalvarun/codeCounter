from django.shortcuts import render, redirect, render_to_response, get_object_or_404

from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

