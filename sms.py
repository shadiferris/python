from twilio.rest import Client

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+NUMBER',
  body='HELLO!!!',
  to='+PHONE_NUMBER'
)

print(message.sid)
