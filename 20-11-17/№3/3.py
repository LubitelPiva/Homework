c = input().split()
N = int(c[0])
minn = 10000
b = 100000000
a = [10000, 10000, 10000, 10000, 10000, 10000]
for i in range(1, N + 1):
	if minn > a[5]:
		minn = a[5]
	a[5] = a[4]
	a[4] = a[3]
	a[3] = a[2]
	a[2] = a[1]
	a[1] = a[0]
	a[0] = int(c[i])
	if b > minn * a[0]:
		b = minn * a[0]
print(b)