import harvestJob
import jobSelection
import jobWriter


import time # Timer (built-in from Python)

SleeperTime = 120;
HoursWait = 4.5;

#print("Sleeping for {} hours ({} seconds) before rising to hunt.\n".format(HoursWait, HoursWait*3600));
#time.sleep(HoursWait*3600);


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

# Repeat the above every X minutes (right now X=5)
	print("Off to sleep for {} minutes before harvesting again.\n".format(SleeperTime/60));
	time.sleep(SleeperTime);

while(True):
	harvestAPEmain();