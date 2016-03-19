---
layout: page
title:  "Exercises 01"
author: paulnguyen
categories: exercises
---

# Problem 3

{% highlight python %}
# get user input and save it to seq
seq = input("Enter a DNA sequence: ")

# four variables to store the base counts
count_A = 0
count_G = 0
count_C = 0
count_T = 0

# loop through all the bases in the sequence
for base in seq:
    if base == "A":  # if we find an A
        count_A += 1 # then update our count of A's
    if base == "G":  # if we find a G
        count_G += 1 # then update our count of G's
    if base == "C":  # etc...
        count_C += 1
    if base == "T":
        count_T += 1

# print all the counts on one line
print(count_A, count_G, count_C, count_T)
{% endhighlight %}