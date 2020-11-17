abbr = input()
N = int(input())
FIO = []
nn = []
for i in range(0, N):
	word = input().split()
	if word[0][0] == abbr[0] and word[1][0] == abbr[1] and word[2][0] == abbr[2]:
		a = 0
		for k in range(0, len(FIO)):
			if word == FIO[k]:
				nn[k] += 1
				a = 1
		if a == 0:
			nn.append(1)
			FIO.append(word)
for i in range(0, len(FIO) - 1):
	for k in range(0, len(FIO) - i - 1):
		if nn[k] < nn[k + 1]:
			a = nn[k]
			nn[k] = nn[k + 1]
			nn[k + 1] = a
			a = FIO[k]
			FIO[k] = FIO [k + 1]
			FIO[k + 1] = a
for i in range(0, len(FIO)):
	if nn[i] > 1:
		print(FIO[i] + " " + str(nn[i]))