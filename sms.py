from twilio.rest import Client

account_sid = 'AC5e0cb34036184dd710fa475d434475ac'
auth_token = '068d38c1c97da4edfddb0a879a7521b0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14176092691',
  body='HELLO!!!',
  to='+61414543296'
)

print(message.sid)