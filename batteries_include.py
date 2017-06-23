colorSet = {'Red', 'Green', 'Red'}

print(colorSet)

a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))
print(a & b)
print(a - b)

my_sets = []
for i in range(10):
	my_sets.append(set(range(i, i+5)))

#print(my_sets)

from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
print(data)
heap = []
for n in data:
	heappush(heap, n)
print(heap)

print(heappop(heap))
print(heappop(heap))

from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
q.pop()
q.popleft()
print(q)
q.rotate(1)
print(q)
q.rotate(-1)
print(q)

values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]
shuffle(deck)
print(deck)

import shelve
s = shelve.open('test')
#temp = s['x']
#s['x'] = ['a', 'b', 'c']
#s['x'].append('d')
#s.close()
print(s['x'])

import re
some_text = 'alpha, beta,,,,gamma delta'
print(re.split('[, ]', some_text))
print(re.split('[, ]', some_text))

print('2 + 3 = [2+3]')
