from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import conf
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

def redirect(request):
	context = RequestContext(request)
	return HttpResponseRedirect('', context)

def index(request):
	context = RequestContext(request)
	return render_to_response('notify/index.jade', context)

def register(request):
	context = RequestContext(request)
	return render_to_response('notify/register.jade', context)	
