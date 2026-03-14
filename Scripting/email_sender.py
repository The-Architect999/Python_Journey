#sending Email with Python
import smtplib #allows us to create an smtp server
# to have a server that communicated the language of the email
# communication beetween browser and the server
from email.message import EmailMessage
from pathlib import Path
# in order to substitute the html$
from string import Template
#direct Path as it is in the same folder
template = Template(Path("index.html").read_text())
# 1. Build the Envelope (The Object)
email = EmailMessage()
email['from'] = 'pyhtonscripterbot@gmail.com'
email['to'] = 'me@gmail.com'
email['subject'] = 'Arise!'
# 2. Write the Payload
# when substituting the subsittute() can also be a dict ({})
# se we can have multiple subs ({name: x, age: 0})
email.set_content(template.substitute({'name': 'Joy'}), subtype='html')

# 3. Connect to the Google SMTP Server
# We use a 'with' block so the connection 
# safely closes itself when finished
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # 4. Wake up the server and encrypt the connection
    smtp.ehlo_or_helo_if_needed()
    # This encrypts the data so no one can intercept it
    smtp.starttls()
     # 5. Login using your Google email and your 16-digit APP PASSWORD 
     # (not your real password)
    # Never hardcode passwords in a real app, 
    # but this is fine for a local test!
    smtp.login('pyhtonscripterbot@gmail.com', 'hello git scraper, i am learning how to build you')
    # 6. Fire the payload
    smtp.send_message(email)
    print('done my leige!')



