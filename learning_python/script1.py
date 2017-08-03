# A first Ptthon script
import sys
print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)
#keyin = input('Enter your name: ')
#print('Hello, ', keyin)

# cmd py script1.py > saveit.txt
# cmd py -3 script1.py

import my_card
from imp import reload
reload(my_card)

import myfile
print(myfile.title)

from myfile import title
print(title)

import threenames
print(threenames.a, threenames.b, threenames.c)

print(dir(threenames))

print(open('my_card.py').read())
exec(open('my_card.py').read())
#print(threenames.__builtins__)