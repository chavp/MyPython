minutes = 105
print(minutes / 60)

hours = minutes // 60
print(hours)

ramainder = minutes - hours * 60
print(ramainder)

x = 9
if x > 0:
	print('x is positive')
elif x == 0:
	print('x is zero')
else:
	print('x is negative')

if 0 < x < 10:
	print('0 < x < 10')

#your_name = input('What is your name?')
#print('Hello,', your_name, '.')
import time
print(time.time())

def check_fermat(a, b, c, n):
	lt = a ** n + b ** n 
	rt = c ** n
	if lt == rt:
		return True
	else:
		return False

def print_fermat(a, b, c, n):
	if n > 2 and check_fermat(a, b, c, n):
		print('Holy smokes, Fermat was wrong! {} {} {} {}'.format(a, b, c, n))
	else:
		print('No, that doesn’t work.')

limit = 3
for n in range(3, limit):
	for a in range(1, limit):
		for b in range(1, limit):
			for c in range(1, limit):
				print_fermat(a, b, c, n)
def recurse(n, s):
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)

recurse(3, 0)

import turtle
t = turtle.Turtle()

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)

draw(t, 3, 11)
turtle.mainloop()