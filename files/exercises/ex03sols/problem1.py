seq1 = input("Enter sequence 1: ")
seq2 = input("Enter sequence 2: ")

purines = ["A", "G"]
pyrimidines = ["C", "T"]
mutationLocations = []

transitionCount = 0
transversionCount = 0

for index in range(0, len(seq1)):
	if seq1[index] != seq2[index]:
		if seq1[index] in purines and seq2[index] in purines or \
				seq1[index] in pyrimidines and seq2[index] in pyrimidines:
			transitionCount += 1
		else:
			transversionCount += 1
		mutationLocations.append(index+1)

if (transversionCount > 0):
	print("The transition/transversion ratio is " + \
			str(transitionCount/transversionCount) + ".")
else:
	print("No transitions were found.")
locations = ""
for loc in mutationLocations:
	locations += str(loc) + ", "
if len(mutationLocations):
	print("Mutations occured at locations " + locations[:len(locations)-2] + ".")
