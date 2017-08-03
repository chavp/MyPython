import math

def sqrt1(a, x):
	epsilon = 0.0001
	y = (x + a/x) / 2
	if abs(x - y) < epsilon:
		return y
	return sqrt1(a, y)

print(sqrt1(5, 2))
print(math.sqrt(4))
print(sum([1,2]))

def my_fun(k):
	return ( math.factorial(4*k) * (1103 + 26390*k) ) / ( (math.factorial(k) ** 4) * (396 ** (4*k) ) )
def my_pi(k):
	a = (2 * math.sqrt(2)) / 9801
	s = sum([my_fun(x) for x in range(k)])
	return 1 / (a * s)

print(math.pi)
print(my_pi(11))

s = 'spam'
t = list(s)
print(t)

verb = dict()
verb['cat'] = '555'


def  hist(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] = d[c] + 1
	return d

print(hist('brontosaurus'))

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

print(invert_dict(hist('brontosaurus')))