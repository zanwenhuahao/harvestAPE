import requests
from lxml import html

#log-in information for automation, where payload is a dictionary
payload = {
	#login information
	"txtUserName" : "zanwenhuahao",
	"txtPassword" : "laotaitai",
	#CSRF token?
}
# the URL to apply to education login page
loginURL = "https://applytoeducation.com/AttLogin.aspx"
# the URL to the job board for parsing supply jobs
harvestURL = "https://www.applytoeducation.com/Applicant/AttOccasionalPostings.aspx?TAB=JB"

testingURL = "https://www.applytoeducation.com/Applicant/AttStart.aspx"

def main():
	#create a session object to keep myself logged in
	loginSession = requests.session()

	loginPage = loginSession.get(loginURL)
		#login
	#result = loginSession.post(loginURL, data = payload)

	#TESTING: print page loaded after login.
	#result = 

	print(loginPage)
	print(loginPage.content)

if __name__ == '__main__':
	main()