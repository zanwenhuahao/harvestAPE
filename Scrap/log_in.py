import requests
import re
from lxml import html

loginURL = "https://applytoeducation.com/AttLogin.aspx"
harvestURL = "https://www.applytoeducation.com/Applicant/AttOccasionalPostings.aspx?TAB=JB"

#Testing that the post request was successful
#This should print the html of the account summary page
#URL of the account summary page after log in
testingURL = "https://www.applytoeducation.com/Applicant/AttStart.aspx"
tdTag = "<td>"
jbTag = "TAB=JB"
paTag = "TAB=PA"
apTag = "TAB=AP"
compTag = "Completed"
accTag = "Accepted"
openTag = "Open"
closedTag = "Closed"
tdEndTag ="</td>"

loginSession = requests.session()

#Get all necessary information to input into form
allInfo = loginSession.get(loginURL)
allInfo_html = html.fromstring(allInfo.text)
hidden_inputs = allInfo_html.xpath(r'//form//input[@type="hidden"]')
# print(hidden_inputs)
allHidden = {x.attrib["name"]:x.attrib["value"] for x in hidden_inputs}
#print(allHidden)

payload = allHidden
payload['txtUserName']='zanwenhuahao'
payload['txtPassword']='laotaitai'
payload['btnLogIn'] = 'LOGIN'
payload['chkRemember'] = ''

#print(payload)
#Logging in
loginResult = loginSession.post(loginURL, data=payload)
# DEBUG: testing if login with payload is successful by 
# printing the url of the page after submit
#print(loginResult.url)
# NOTE: the url printed is a browserNotSupported.asp, however, login is successful
# and the script can proceed to get authenticated pages

# -----------------------------
# Get the information on account summary page after logging in
#loginResult = loginSession.get(testingURL)

# DEBUG: testing that loginPage is the account summary page's html
#print(loginResult.text)
# -----------------------------

# -----------------------------
# Get EasyConnect Job Board page
loginResult = loginSession.get(harvestURL)

# Gets HTML of all 3 tabs under EasyConnect. The jobs that are currently
# listed on Job Board has <TAB=JB> as part of the table element

# Writing all EasyConnect page HTML to the loginTest file.
loginHTML = open("loginTest.txt","w")
loginHTML.write(loginResult.text)
loginHTML.close()
# -----------------------------

# -----------------------------
# From all EasyConnect page's HTML file, parse out the HTML lines with each job
# Testing currently with TAB=PA as there may or may not be jobs on Job Board

tdlines = open("readline.txt","w")
with open("loginTest.txt","r") as readin:
	line = readin.readline()
	while line:
		if tdTag in line and jbTag in line:
			for x in range(0,7):
				line = line.strip()
				if line != "":
					tdlines.write(line)
					tdlines.write("\n")
				line = readin.readline()
		line = readin.readline()
readin.close()
tdlines.close()
# -----------------------------

# -----------------------------
#read in HTML of all valid jobs into a string to work with
resultHTML=""
with open("readline.txt","r") as resultLines:
	line = resultLines.readline()
	while line:
		resultHTML = resultHTML + line
		line = resultLines.readline()
resultLines.close()

# -----------------------------

# -----------------------------
# Interesting technique: replace all close tag with an extra space so when
# parsing with text_content function, the space between text is produced
# (so texts between tags that do not have space aren't glued together into one word)
resultHTML = re.sub("</", " </", resultHTML)
resultHTML = re.sub("/>", "/> ", resultHTML)
# finalHTML = ""
# for eachline in resultHTML.split("\n"):
# 	eachline = eachline.lstrip()
# 	finalHTML = finalHTML+eachline+"\n"

# print(finalHTML)
# Convert the result into a html document to use lxml library
# If debugs if there are No Current Jobs (i.e. program doesn't crash)
if(resultHTML != ""):
	result = html.fromstring(resultHTML)
# Using lxml library to take content of HTML of valid jobs only
	result = result.text_content()
	# Formatting finalResult so it looks nice, properly spaced and newlined
	finalResult = ""
	for eachline in result.split("\n"):
		eachline = eachline.strip()
		if eachline != "":
			finalResult = finalResult+eachline+"\n"
		if eachline in (compTag, accTag, openTag, closedTag):
			finalResult = finalResult + "\n"
else:
	finalResult = "No Current Jobs\n"

print(finalResult)

# ----------------------------
# resultList = result.split()
# print(resultList)

# Printing the results to a text document
jobsOut = open("curJobs.txt","w")
jobsOut.write(finalResult)
jobsOut.close()

# END of job harvesting program

