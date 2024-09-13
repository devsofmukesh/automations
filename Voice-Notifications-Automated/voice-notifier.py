# Import necessary libraries
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# Add your Account SID and Authorization Token
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_ACCOUNT_AUTH_TOKEN"

# Initialize the Twilio Client with your credentials
client = Client(account_sid, auth_token)  

# Create a VoiceResponse object to build a customized voice message
response = VoiceResponse()
voice_message = "I wish you enjoy your evening with joy and laughter, \
peace at your heart because my brother these are the things that you truly deserve."

# Add the spoken message to the response
response.say(voice_message)

# Make a call to the target number using Twilio; replace with your actual numbers
call = client.calls.create(twiml=response, to=['+919741235707'], from_='+19292388701')

# Print the unique SID of the call to confirm it was successfully created
print("Unique ID:", call.sid)