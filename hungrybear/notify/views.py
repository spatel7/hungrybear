from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from notify.models import UserProfile
from django import conf
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.contrib import messages
from notify.forms import UserForm, UserProfileForm
from notify.verify import send_verification

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
		uprofile_form = UserProfileForm(data=request.POST)
		user_form = UserForm(data=request.POST)
		#import pdb; pdb.set_trace()
		if uprofile_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			userProfile = uprofile_form.save(commit=False)
			userProfile.user = user
			#userProfile.phone = request.POST['phone']
			#userProfile.save()
			#make twilio send verification code & associate it with phone number
			number = "+" + str(userProfile.phone.country_code) + str(userProfile.phone.national_number)
			#import pdb; pdb.set_trace()
			code = send_verification(number)
			print code #for testing purposes
			userProfile.verification_num = code
			userProfile.save()
			request.session['uprofile'] = userProfile.user.id
			registered = True
			return render_to_response('notify/confirm.html', context)
		else:
			if not uprofile_form.is_valid():
				for k,v in uprofile_form.errors.iteritems():
					messages.error(request, v)
			if not user_form.is_valid():
				for k,v in user_form.errors.iteritems():
					messages.error(request, v)
			print uprofile_form.errors
			print user_form.errors
	else:
		uprofile_form = UserProfileForm()
		user_form = UserForm()
	return render_to_response('notify/register.html', context)	

def confirm(request):
	context = RequestContext(request)
	if request.method == 'GET':
		return HttpResponseNotFound('Page not found')
	elif request.method == 'POST':
		#import pdb; pdb.set_trace()
		print "hmm"
		userProfile = UserProfile.objects.get(user=User.objects.get(id=request.session['uprofile']))
		if int(request.POST['code']) != userProfile.verification_num:
			print "welp?"
			messages.error(request, 'Incorrect verification code.') #message ending up on intial register page... something to do with context??
			#implement resend option?
		else:
			print "success"
			userProfile.verified = True
			userProfile.save()
			import pdb; pdb.set_trace()
			return render_to_response('notify/create.html', context) #not rendering...
	return render_to_response('notify/confirm.html', context)