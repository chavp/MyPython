def fibs(num):
	results = [0, 1]
	for i in range(num - 2):
		results.append(results[-2] + results[-1])
	return results

print(fibs(10))

def hello(name):
	'Hello, name'
	return 'Hello, {}'.format(name)

print(hello('Ding'))

print(hello.__doc__)

names = ['Mrs. Entity', 'Mrs. Thing']
print(names[:])

def inc(x): return x + 1

print(inc(100))

def add(x, y): return x + y

p1 = (1, 2)

print(add(*p1))

params = {'name': 'Sir Robin', 'greeting': 'Well met'}

def mul(fac):
	def myFac(num):
		return fac * num
	return myFac

print(mul(2)(5))

def factorial(n):
	results = n
	for i in range(1, n):
		results *= i
	return results

def re_factorial(n):
	if n == 1: return 1
	return n * re_factorial(n-1)

print(re_factorial(5))

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce

r = reduce(lambda x, y: x + y, numbers)

print(r)