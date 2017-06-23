import sys, pprint
sys.path.append('D:\my-code\MyPython')

# pprint.pprint(sys.path)

from hello import talk

talk()

import copy

results = [n for n in dir(copy) if not n.startswith('_')]
print(results)
print(copy.__all__)