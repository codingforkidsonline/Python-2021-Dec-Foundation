```python

# Question 1 Answer:
from random import random

r = random()
print(r)



# Question 2 Answer:
import random

r = random.randint(1, 10)
print(r)




# Question 3 Answer:
from datetime import datetime

current_time = datetime.now()
print("current time is:", current_time)




# Question 4 Answer:
sentence = "The pythons are a family of nonvenomous snakes found in Africa Asia and Australia"

word_list = sentence.split()

s = ""
for w in word_list:
  s += w[0]

print(s)




# Question 5 Answer:
sentence = "The notion that the Great Wall can be seen from the moon is a well-known but implausible myth"

count = 0
for c in sentence:
  if c == "t" or c == "T":
    count += 1

print(count)




# Question 6 Answer:
def calculate_sum(a, b):
  sum = a + b
  return sum

result1 = calculate_sum(10, 20)
print(result1)

result2 = calculate_sum(47, 53)
print(result2)




# Question 7 Answer:
def compare_number(a, b):
  if a == b:
    return "equal"
  else:
    return "not equal"

result1 = compare_number(33, 34)
print(result1)

result2 = compare_number(555, 555)
print(result2)




# Question 8 Answer:
n_str = input("Please key in a number greater than 1:")

n = int(n_str)

if n < 2:
  print("Invalid Number")
else:
  result = "Yes"
  for i in range(2, n):
    if n%i == 0:
      result = "No"
      break
  print(result)


```
