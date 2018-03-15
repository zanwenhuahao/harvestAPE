#simply reads each line in a file that are between <tr> tags
tdcounter = 0
tdlines = ""
with open("loginTest.txt","r") as readin:
	line = readin.readline()
	while line:
		if "<td>" in line and "TAB=PA" in line:
			tdlines = tdlines + line + "\n"
		line = readin.readline()
readin.close()
print(tdlines)
			







