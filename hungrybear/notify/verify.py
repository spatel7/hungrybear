from twilio.rest import TwilioRestClient
from django.conf import settings

import os

account_sid = "AC9cf13d04ad88f29b655bda4293236559"
auth_token = "db6d278e0f69a3b159ab6d9954025cad"
client = TwilioRestClient(account_sid, auth_token)

def random_generate():
	#randomly generate a verification code; either return a string or cast code to str
	return 0;

def send_verification(phone_number):
	code = random_generate()
	client.messages.create( 
		body="Hello! Thanks for joining Hungry Bear! Here is the verification code for your number: " + code
		to=str(user_profile.phone[national??]]) #temp
		from_="+15108086075", 
	)