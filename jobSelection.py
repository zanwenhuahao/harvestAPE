import emailSetUp

def jobSelect():
	allID = open("jobsID.txt","r")
	jobLst = []

	#Reading lines into list to check for new jobs
	line = allID.readline()
	while line:
		jobLst = jobLst + [line[0:7]]
		line = allID.readline()
	allID.close()

	#curJobs.txt should contain the all jobs in the most recent query
	curJobs = open("curJobs.txt", "r")
	line = curJobs.readline()
	jobID = ""
	newJob = ""
	while line:
		jobID = line[0:7]
		if jobID.isdigit() and jobID not in jobLst:
			while line!="":
				newJob = newJob + line
				line = curJobs.readline()
		line = curJobs.readline()
	curJobs.close()

	#Testing that only the new job is printed
	#print(newJob)

	# Write the new job to file to be emailed to self
	newJobFile = open ("newJob.txt", "w")
	newJobFile.write(newJob)
	newJobFile.close()
	if newJob!="":
		emailSetUp.emailJob()