vowels = ["A", "E", "I", "O", "U"]

string = "facetiously"
vowel_count = 0
for char in string.upper():
	if char in vowels:
		vowel_count += 1
print("The number of vowels is: " + str(vowel_count))
