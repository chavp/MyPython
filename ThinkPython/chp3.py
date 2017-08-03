print(type(42))
print(type('32'))
print(type(int('32')))
print(float(32))
print(int(32.3))

import math
print(type(math))

print(math.log10(100))
print(math.pi)

degree = 45
x = math.sin(degree / 360.0 * 2 * math.pi)
print(x)
x = math.exp(math.log(x + 1))
print(x)

def print_lyrics():
	print('I\'m a lumberjack...')
	print('I sleep ...')

print_lyrics()

golden = (math.sqrt(5) + 1) / 2
print(golden)

def draw_box(n):
	for x in range(n-1):
		print('+', '-' * n, '+', '-' * n, '+')
		if x < n-2:
			for y in range(n):
				print('|', ' ' * n, '|', ' ' * n, '|')

draw_box(4)

import turtle
wn = turtle.Screen()

bob = turtle.Turtle()
#print(bob)
def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90)

def polygon(t, n, length):
	angle = 360 / n
	polyline(t, n, length, angle)

def circle(t, r):
	arc(t, r, 360)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * math.fabs(angle) / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n
	polyline(t, n, step_length, step_angle)

def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

#square(bob)
#polygon(bob, n=7, length=70)
#circle(bob, r=70)
#arc(bob, r=70, angle=360)
#polyline(bob, n=8, length=70, angle=45)

# Exercise 4-2.
arc(bob, r=100, angle=70)

turtle.mainloop()