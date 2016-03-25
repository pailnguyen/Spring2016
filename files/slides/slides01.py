# Week 1 Test Program Reference
# Paul Nguyen - Spring 2016

print("Hello world!")

pi = 3.14159
greeting = "Bonjour."

number = 2
print(number)
number = 7 * 7
print(number)
number = "This is a string."
print(number)

x = 4
print(x)
x = x + 2
print(x)
x += 2
print(x)

string_one = "Hello "
string_two = "world!"
print(string_one + string_two)

number = 3
# number = 4
print(number) # TODO: add new features

name = input("Enter your name: ")
print("Hello " + name + "!")

3 > 2 # returns True
3 < 2 # returns False

1 + True # can you guess what happens?
3 + False # what happens here?

x = 5
if x > 2:
	print("x is greater than 2")

if 238:
	print("success 1!")

if 0:
	print("success 2!")

if -49:
	print("success 3!")

name = input("Please enter your name: ")
if name == "Paul":
    print("Greetings, " + name + "!")
else:
    print("Hello, " + name + ".")

grade = 97
if grade > 90:
    if grade > 93:
        if grade > 97:
            print("Grade = A+")
        else:
            print("Grade = A")
    else:
        print("Grade = A-")
else:
    print("Grade is less than A-")

if name == "Paul":
    print("Greetings, " + name + "!")
elif name == "Farzam":
    print("Salutations, " + name + "!")
else:
	print("Hello, " + name + ".")

x = 20
if x > 5 and x < 21:
	print("Success 1")
	# "Success 1" is printed
if x > 5 and x > 21:
	print("Success 2")
	# "Success 2" is not printed

x = 20
if x > 5 or x < 21:
	print("Success 1")
	# "Success 1" is printed
if x < 5 or x < 21:
	print("Success 2") # "Success 2" is printed even though the first condition 
					   # is false
if x < 5 or x > 21:
	print("Success 3") # "Success 3" is not printed

x = 20
print(x > 3) # prints "True"
print(not (x > 3)) # prints "False"
if x > 5 or x < 21:
	print("Success 1") # "Success 1" is printed
if not (x > 5 or x < 21):
	print("Success 2") # "Success 2" is not printed

a = [] # empty list
b = [2, 3, 5, 7]
c = ["Hello", "Goodbye"]
d = ["Hello", 32] # lists can contain items of different types

string_one = "ABCDEFG"
string_one[1] # returns "B"

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	print(fruit)
	
numbers = [2, 3, 4, 5]
for number in numbers:
	number = number * 2
	print(number)
print(numbers)

vowels = "AEIOU"
string = "facetiously"
vowel_count = 0
for letter in string.upper(): # check over the uppercase version of the string
	if letter in vowels:
		vowel_count += 1
print("The number of vowels is: " + str(vowel_count))

x = 0
while x <= 5:
	print(x, x*x)
	x += 1
