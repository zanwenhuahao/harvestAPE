#simply reads each line in a file that are between <tr> tags
trcounter = 0
trlines = ""
with open("loginTest.txt","r") as readin:
	line = readin.readline()
	while line:
		if trcounter == 1:
			trlines = trlines + line
		else:
			if "<tr" in line and "</tr>" not in line:
				trcounter = 1
				trlines = trlines + line
			if trcounter == 1 and "</tr>" in line:
				trcounter = 0
				trlines = trlines + line
			if "<tr" in line and "</tr>" in line:
				trcounter = 1
		line = readin.readline()
readin.close()
print(trlines)
			







