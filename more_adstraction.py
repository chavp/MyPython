name = 'Pariny Chavanasuvarngull'

print(name.count('a'))

from random import choice
x = choice(['Hello, world!', [1, 2, 'e', 'e', 4]])

print(x.count('e'))

# Polymorphism

def add(x, y):
	return x + y

print(add(1, 2))
print(add('Hello', 'World'))

print(repr([1, 2, 3]))
print(repr(add('Hello', 'World')))

class Person:
	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def greet(self):
		print('Hello, {}'.format(self.get_name()))

ding = Person()

ding.set_name('Ding')
print(ding.get_name())

ding.greet()

class Secret:
	def __pri(self):
		print("Can't access")
	def pub(self):
		print('Can access')
		self.__pri()

se = Secret()
se.pub()

class MemCount:
	count = 0
	def init(self):
		MemCount.count += 1

mc1 = MemCount()
mc1.init()
print(mc1.count)

mc2 = MemCount()
mc2.init()
print(mc2.count)

class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class TheFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

t = TheFilter()
t.init()
fil = t.filter(['SPAM', 'SPAM', 'ding', 'parinya', 'SPAM'])
print(fil)

print(issubclass(TheFilter, Filter))

class Calculator:
	def cal(self, expression):
		self.value = eval(expression)

class Talk:
	def talk(self):
		print('My value is {}.'.format(self.value))

class CalculatorTalk(Calculator, Talk):
	pass

ct = CalculatorTalk()
ct.cal('2 + 3 * 5')
ct.talk()

# Abstract base class
from abc import ABC, abstractmethod

class Talker(ABC):
	@abstractmethod
	def talk(self):pass

class Knigget(Talker): 
	def talk(self):
		print('5555')

k = Knigget()
k.talk()