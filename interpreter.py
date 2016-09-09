fhand = open("pokeData.txt")

stateCategory = list()
stateCategory.append("Null")
state1 = list()
state2 = list()

for line in fhand:
	words = line.split(",")
	word = words[0].strip()
	if word not in stateCategory:
		stateCategory.append(word)
	state1.append(stateCategory.index(word))
	word = words[1].strip()
	if word not in stateCategory:
		stateCategory.append(word)
	state2.append(stateCategory.index(word))

print state1
print state2