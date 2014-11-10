from subprocess import call
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View, CreateView
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

class Index(TemplateView):
  template_name = 'index.html'



def deploy(request):
	ex = "nothing"
	if request.method == 'POST':
		ex = "post"
		try:
			call(["/bin/sh","/home/django/django_project/heron/deploy.sh"])
			ex = "called"
		except Exception as e:
			ex = e
		
	return render(request, 'deploy.html', {'ex': ex})
