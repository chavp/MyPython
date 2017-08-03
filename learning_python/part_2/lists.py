L = [123, 'spam', 1.23]
print(len(L))

print(L[0])
print(L[:-1])

L = L + [4, 5, 6]
print(L[1:3])
print(L * 2)

L.append('NI')
print(L)
L.pop(2)
print(L)

M = ['bb', 'aa', 'cc']
#M = M.sort()
print(M)

M2 = [i*2 for i in M]
print(M2)

S1 = [i for i in range(1, 100) if i % 2 == 0]
print(S1)

doubles = [c*2 for c in 'spam']
print(doubles)

S2 = [(i, j) for i in range(5) for j in range(3) if i%2 == 0 if j%2 == 1]
print(S2)

def plus_1(a):
	return a + 1

def plus_3(a):
	return a + 3

S3 = [1, 2, 3]
print(list(map(plus_3,  S3)))