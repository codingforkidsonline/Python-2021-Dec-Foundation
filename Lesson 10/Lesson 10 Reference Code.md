```python

# we can use dir() function to list all the function names 
# and vairable names in a module

import math

dir(math)



# use random module to generate a random number

import random

# generate a random between 0.0 to 1.0
r = random.random()
print(r)



# only import randint() function from random module

from random import randint

# generate a random integer from 1 to 100
r = randint(1, 100)
print(r)



# use datetime class in datetime module to 
# diplay the current date time (UTC time)

from datetime import datetime

current_time = datetime.now()
print(current_time)



# define a function to calculate the average value of two numbers
def average(a, b):
  sum = a + b
  ave = sum/2
  return ave

# call the function 1st time
result1 = average(1, 2)
print("result 1 is:", result1)

# call the function 2nd time
result2 = average(10, 20)
print("result 2 is:", result2)



# Secret Message
# use input() to capture the message
sentence = input("write a sentence to Sam the Cat with your hidden secret message: ")
print(sentence)

# use split() to split the sentence into multiple words in a word list
word_list = sentence.split()
print(word_list)

# use a for loop to take the first character of each word
secret_message = ""

for w in word_list:  
  secret_message += w[0]

print(secret_message)



# Crazy Dog
# define a function to count the number of E or e
def countE(s):
  count = 0
  # use for loop to check each character in s, 
  # if it is e or E, increase the count
  for c in s:
    if c.upper() == "E":
      count += 1
  return count


# use input the capture the sentence
sentence = input("please give me your message: ")

number_of_e = countE(sentence)

print(number_of_e)

# use if/elif/else to output Greg's reaction based on the count
if number_of_e == 0:
  print("Happy!")
elif number_of_e < 4:
  print("sad")
else:
  print("CRAZY!")
  
  
  
# Dog Treats
a = 1   #first day
b = 1   #second day

treats = []

treats.append(a)
treats.append(b)

for i in range(18):
  fibo = a + b
  treats.append(fibo)
  a = b
  b = fibo

print(treats)
# check if your answer is same as below:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]



# Bag of Bones
number_str = input("Please input the number of bones in the bag: ")

# convert a string to a number
number = int(number_str)

if number < 4 or number > 100:
  print("Invalid number!")
else:
  possible = False
  for i in range(2, number):
    if number % i == 0:
      possible = True
      break

  if possible:
    print("Yes")
  else:
    print("No")


```
