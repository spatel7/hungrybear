from twilio.rest import TwilioRestClient
from django.conf import settings
from random import randint
import os

account_sid = "AC9cf13d04ad88f29b655bda4293236559"
auth_token = "db6d278e0f69a3b159ab6d9954025cad"
client = TwilioRestClient(account_sid, auth_token)

def random_generate(n):
	#randomly generate a six digit verification code; either return a string or cast code to str
	start_range = 0
	end_range = 10**(n)-1
	return randint(start_range, end_range)

def send_verification(phone_number):
	code = random_generate(6)
	client.messages.create( 
		body="Hello! Thanks for joining Hungry Bear! Here is the verification code for your number: " + str(code),
		to= phone_number,
		from_="+15005550006"
	)
	return code