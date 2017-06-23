def div(a, b):
	if b == 0: raise ZeroDivisionError('b can not Zero.')

try:
	div(1, 0)
except (ZeroDivisionError):
	print('zero div')
except (Exception) as e:
	print(e)
finally:
	print('Fin')

def faulty():
	raise Exception('Something is wrong!')

def ignore_exception():
	faulty()

def  handle_exception():
	try:
		faulty()
	except:
		print('Exception handle.')

# ignore_exception
handle_exception()



