d = {}
d.setdefault('name', 'null')

print(d['name'])

d['name'] = 'ding'
d['title'] = 'Mr'

print(d['title'], d['name'], sep='_')

import math as football

print(football.sqrt(2))

from math import sqrt
print(sqrt(3))

x, y, z = 1, 2, 3
print(x, y, z)

vals = 1, 2, 3
print(vals)

a, b, *rest = [1, 2, 3, 5]

print(rest)

full_name = 'Mr Parinya Chav'

title, first, last = full_name.split()

print(first)

x = 2
x += 1
x *= 3
print(x)

if x == 2 :
	print('Ok')
elif x == 9:
	print('Ok'*2)
else:
	print('Not Ok')
print('-'*100)
names = ['Anne', 'Beth', 'George', 'Damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
	print('{0} is age {1} years old.'.format(names[i], ages[i]))
print('-'*100)
for name, age in zip(names, ages):
	print('{0} is age {1} years old.'.format(name, age))


even10 = [x for x in range(10) if x % 2 == 0]
print(even10)