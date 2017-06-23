class Foo(object):
	"""docstring for Foo"""
	def __init__(self):
		self.value = 40

f = Foo()
print(f.value)

class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print('Aaaah...')
			self.hungry = False
		else:
			print('No I am full')

bird = Bird()
bird.eat()
bird.eat()

class SongBird(Bird):
	def __init__(self):
		# Bird.__init__(self)
		super().__init__()
		self.sound = 'Squawk!'
	def  sign(self):
		print(self.sound)

b2 = SongBird()
b2.sign()
b2.eat()
b2.eat()

class MyArray:
	def __init__(self):
		self.numbers = [1, 2, 3, 4, 5]
	def __getitem__(self, key):
		try:
			return self.numbers[key]
		except:
			return 0
	def __setitem__(self, key, value):
		try:
			self[key] = value
		except:
			pass

myArray = MyArray()
print(myArray[1])
print(myArray[10000])


class CounterList(list):
	def __init__(self, *args):
		super().__init__(*args)
		self.counter = 0
	def __getitem__(self, index):
		self.counter += 1
		return super(CounterList, self).__getitem__(index)

c = CounterList(range(100))
del c[30:50]
print(c.counter)
cal = c[1] + c[10]
print(c.counter)

def flatten(nested):
	try:
		for sublist in nested:
			for elm in flatten(sublist):
				yield elm
	except TypeError:
		yield nested

nested = [[1, 2], [3], [4,5, [6, 7]], [8], 9, 10]

print(nested)
print(list(flatten(nested)))

g = ( (i + 2) ** 2 for i in range(2, 27) )
# print(list(g))
print(next(g), next(g), next(g))
print(sum(g))