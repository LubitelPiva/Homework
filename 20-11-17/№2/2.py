N = int(input())
a = 10000
b = 10000
an = 0
bn = 0
c = input().split()
for i in range(0, N):
	if a > int(c[i]):
		b = a
		bn = an
		a = int(c[i])
		an = 1
	else:
		if b > int(c[i]):
			b = int(c[i])
			bn = 1
		else:
			if a == int(c[i]):
				an += 1
			elif b == int(c[i]):
				bn += 1
print(str(a + b) + " " + str(an * bn))