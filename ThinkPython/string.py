fruit = 'banana'
print(len(fruit))

index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

# slice
print(fruit[:3])
print(fruit[3:])

import string
import random

rans = [random.random() for x in range(10)]
print(rans)

t = [x for x in range(10)]
print(random.choice(t))