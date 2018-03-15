#smtp library
import smtplib #smtp library
from datetime import datetime

#Python's build in EMAIL library toolkit
# from email.message import EmailMessage 


# Constants:
# Emailing from "myemail@gmail.com" to itself

gmailAddress = 'myemail@gmail.com'
gmailPassword = 'somePassword'

mailFrom = "myemail@gmail.com"
mailTo = "myemail@gmail.com"

# -------------------------------

# Set up the email message (body of message) to be sent
# theEmail = EmailMessage()
# theEmail.set_content(message)
# theEmail['Subject'] = "Testing Testing"
def emailJob():
	dateNow = "{: %B %d, %Y}".format(datetime.now())
	SUBJECT = "[Harvest] Jobs Now - " + dateNow
	curTime = "Time @ {:%X}\n\n".format(datetime.now())
	TEXT = curTime
	with open("newJob.txt", "r") as content:
		TEXT=TEXT+content.read()
	content.close()

	message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)

	# -------------------------------

	# Connecting to gmail's SMTP server and logging in
	try: 
		gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		gmail.login(gmailAddress, gmailPassword)
		gmail.sendmail(mailFrom, mailTo, message)

		print("Mail has been successfully sent!")
		gmail.quit() # Close the SMTP connection

	# If something went wrong with the SMTP connection
	except:
		print("Something went wrong with connecting to gmail's smtp server")

	return;













