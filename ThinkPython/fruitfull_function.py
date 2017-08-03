import math

def area(radies):
	return 2 * math.pi * radies

def factorial (n):
	if not isinstance(n, int):
		print('Factorial is only defined for integers.')
		return None
	elif n < 0:
		print('Factorial is not defined for negative integers.')
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

def a(m, n):
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return a(m - 1, 1)
	if m > 0 and n > 0:
		return a(m-1, a(m, n-1))

print(a(3, 3))