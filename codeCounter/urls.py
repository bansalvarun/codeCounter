"""codeCounter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from apps.demo.views import *
from apps.courseTube.views import *

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^registerAsStudent/', registerAsStudent, name = "registerAsStudent"),
    url(r'^registerAsInstitute/', registerAsInstitute, name = "registerAsInstitute"),
    url(r'^register_institute/', registerInstitute, name = "registerInstitute"),
    url(r'^institute/(?P<id>.+)/', institute, name = "institute"),
    url(r'^institutes/', institutes, name = "institutes"),
    url(r'^tags/', tags, name = "tags"),
    url(r'^tag/(?P<id>.+)/', tag, name = "tag"),
    url(r'^postFeedback/', postFeedback, name = "postFeedback"),
    url(r'^locationsOfInstitues/', locationsOfInstitues, name = "locationsOfInstitues"),

    # url(r'^institutesRequests/', institutesRequests, name = "institutesRequests"),

]
