seq = input("Enter a DNA sequence: ") # get user input and save it to seq
count_A = 0 # four variables to store the base counts
count_G = 0
count_C = 0
count_T = 0

for base in seq:     # loop through all the bases in the sequence
    if base == "A":  # if we find an A
        count_A += 1 # then update our count of A's
    if base == "G":  # if we find a G
        count_G += 1 # then update our count of G's
    if base == "C":  # etc...
        count_C += 1
    if base == "T":
        count_T += 1

print(count_A, count_G, count_C, count_T) # print all the counts on one line
