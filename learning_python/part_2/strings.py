S = 'Spam'
print(len(S))
print(S[0])
print(S[3])
print(S[-1])
print(S[1:3])
print(S[1:]) # slice 1:len(S)
print(S[:2]) # 0:2
print(S + 'xyz')
print(S * 8)

L = list(S)
L.extend('xyz')
print(L)

print(S.find('pa'))
S.replace('xyz', '')
print(S)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

print(S.isalpha())

C = '123123123'
print(C.isdigit())

line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())

print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

print(dir(S))
print(S.__add__('xyz'))
print(help(S.replace))

print(ord('\n'))