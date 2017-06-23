# numberlines.py                                   #  1
                                                   #  2
import fileinput                                   #  3
                                                   #  4
for line in fileinput.input(inplace=True):         #  5
	line = line.rstrip()                              #  6
	num = fileinput.lineno()                          #  7
	print('{:<50} # {:2d}'.format(line, num))         #  8
