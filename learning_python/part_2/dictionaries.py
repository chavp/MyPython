D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)

print(D['food'])

D1 = {}
D1['name'] = 'Ding'
D1['last_name'] = 'Chav'
print(D1)

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

rec = {
	'name': {'first': 'Bob', 'last': 'Smit'},
	'jobs': ['dev', 'mgr'],
	'age': 40.5
}
print(rec)

#rec['555']
if not '555' in rec:
	print('Missing 555')

v555 = rec['555'] if '555' in rec else 'null'
print(v555)
print(rec.keys())

for key in sorted(rec.keys()):
	print(key, '=', rec[key])