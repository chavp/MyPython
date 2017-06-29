import collections as col

# Initialize
print(col.Counter(['a', 'b', 'c', 'a']))

c = col.Counter()
print('Init:', c)

c.update('abcdaab')
print('Seq:', c)

c.update({'a':1, 'd':5})
print('Dic:', c)

# Accesing counter
c = col.Counter('abcdaab')
for letter in 'abcde':
    print('%s : %d' % (letter, c[letter]))

c = col.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

c = col.Counter()
with open('E:\\projects\\MyPython\\adstraction.py') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most common:')
for letter, count in c.most_common(3):
    print('%s: %7d' % (letter, count))

def default_factory():
    return 'default value'
d = col.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

Person = col.namedtuple('Person', 'name age gender')
print('type(Person)', Person)
bob = Person(name='Bob', age=30, gender='male')
print('\nRepresentation:', bob)

import array
import pprint

a = array.array('i', range(3))
print('Initial:', a)
a.extend(range(3))
print('Extend:', a)
