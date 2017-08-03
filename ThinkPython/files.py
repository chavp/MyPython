fout = open('output.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
fout.close()

import os
cwd = os.getcwd()
print(cwd)

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

walk('C:\\Users\\parinya\\Downloads')

import pickle
t =[1, 2, 3]
pickle.dumps(t)

class Rectangle:
	"""
	attributes: width
	"""

box = Rectangle()
box.width = 100.0

print(box.width)