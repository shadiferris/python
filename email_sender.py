'''
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Shadi Ferris'
email['to'] = 'shadiferris@hotmail.com'
email['subject'] = 'you won a $1,000,000 dollars'

email.set_content('Im a python master')

with smtplib.SMTP(host='smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shadi.ferris@gmail.com','shadsta1')
    smtp.send_message(email)
    print('All good Boss!!!')

'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
message = MIMEMultipart()
message["To"] = 'Shadi Ferris'
message["From"] = 'shadi.ferris@gmail.com'
message["Subject"] = 'you won a $1,000,000 dollars'

title = '<b> you won a $1,000,000 dollars!!! </b>'
messageText = MIMEText('''MIm a python master''','html')
message.attach(messageText)

email = 'shadi.ferris@gmail.com'
password = 'shadsta1'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo('Gmail')
server.starttls()

server.login(email,password)
fromaddr = 'shadi.ferris@gmail.com'
toaddrs  = 'shadi.ferris@gmail.com'
server.sendmail(fromaddr,toaddrs,message.as_string())

server.quit()
print("all good!!!")