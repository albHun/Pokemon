fhand = open("PureData.txt")
count = 0
fname = ""
str = ""

for line in fhand:
	count += 1
	str += line
	if count == 480:
		fname = "TraningSet.txt"
		dhand = open(fname, "w")
		dhand.write(str)
		str = ""
	elif count == 640:
		fname = "CrossValidationSet.txt"
		dhand = open(fname, "w")
		dhand.write(str)
		str = ""
	elif count == 800:
		fname = "TestSet.txt"
		dhand = open(fname, "w")
		dhand.write(str)