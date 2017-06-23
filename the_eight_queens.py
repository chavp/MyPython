def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		#print(abs(state[i] - nextX), (0, nextY - i))
		if abs(state[i] - nextX) in (0, nextY - i):
			#print('_' * 6, True, '_' * 6)
			return True
	#print('_' * 6, False, '_' * 6)
	return False

def queens(num, state):
	if len(state) == num-1:
		for pos in range(num):
			#print('conflict', state, pos)
			if not conflict(state, pos):
				yield pos

print( list(queens(4, (1, 3, 2) )) )

def queens_solve(num = 8, state = ()):
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num-1:
				yield (pos,)
			else:
				for result in queens_solve(num, state + (pos,)):
					yield (pos,) + result

# print(list(queens_solve(4)))

def prettyprint(solution):
	def line(pos, length=len(solution)):
		return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
	for pos in solution:
		print(line(pos))

import random
prettyprint(random.choice(list(queens_solve(4))))