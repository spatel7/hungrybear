from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import conf
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.contrib import messages
from notify.forms import phoneForm

def redirect(request):
	context = RequestContext(request)
	return HttpResponseRedirect('', context)

def index(request):
	context = RequestContext(request)
	return render_to_response('notify/index.jade', context)

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		#import pdb; pdb.set_trace()
		phone_form = phoneForm(data=request.POST)
		if phone_form.is_valid():
			userProfile = phone_form.save(commit=False)
			#userProfile.phone = request.POST['phone']
			#userProfile.save()
			#make twilio send verification code & associate it with phone number
			registered = True
			return render_to_response('notify/confirm.html', context)
		else:
			messages.error(request, 'Please enter a valid number')
			print phone_form.errors
	else:
		phone_form = phoneForm()
	return render_to_response('notify/register.html', context)	

def confirm(request):
	context = RequestContext(request)
	if request.method == 'GET':
		return HttpResponseNotFound('Page not found')
	#elif request.method == 'POST':
		#check if submitted verificaiton code matches that associated with number
		#if so, bring them to create user profile page
	return render_to_response('notify/confirm.html', context)