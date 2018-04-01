import harvestJob
import jobSelection
import jobWriter

import time #Timer to execute harvesting every 1 minute.

def harvestAPEmain():
# 1. call harvestJob.py -> returns "curJobs.txt"
	# Note: "jobsID.txt" is initially empty at the
		# beginning of time(or start of each day)
	harvestJob.harvestJob();
# 2. call jobSelection.py (consumes "jobsID.txt" and "curJobs.txt")
	# -> returns "newJobs.txt"
	# -> sends email if "newJobs.txt" is not empty.
	jobSelection.jobSelect();
# 3. call jobWriter.py (consumes curJobs.txt) -> returns "jobsID.txt"
	# (This updates jobsID.txt with IDs of all curJobs)
	jobWriter.writeCurrentJobs();
# Repeat the above every 2 minutes
	time.sleep(60)

while(True):
	harvestAPEmain();