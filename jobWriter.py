def writeCurrentJobs():
	curJobs = open("curJobs.txt", "r")
	jobsID = open("jobsID.txt","w")

	line = curJobs.readline()
	while line:
		if (line[0:7].isdigit()):
			#This is the line with the job ID
			jobsID.write(line[0:7]+"\n")
		line = curJobs.readline()
	jobsID.close()
	curJobs.close()