fhand = open("pokeData.txt")
dhand = open("PureData.txt","w")

stateCategory = list()
stateCategory.append("Null")
state1 = list()
state2 = list()

for line in fhand:
	words = line.split(",")
	
	word = words[0].strip()
	if word not in stateCategory:
		stateCategory.append(word)
	index = stateCategory.index(word)
	for i in range(19):
		if i == index:
			dhand.write("1,")
		else:
			dhand.write("0,")
	
	word = words[1].strip()
	if word not in stateCategory:
		stateCategory.append(word)
	index = stateCategory.index(word)

	for i in range(19):
		if i == index:
			dhand.write("1,")
		else:
			dhand.write("0,")
	
	for i in range(2, (len(words) - 1)):
		word = words[i].strip()
		dhand.write(word + ",")
	dhand.write(words[len(words)-1].strip() + "\n")