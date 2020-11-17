N = int(input())
s = 0
c = 300000
for i in range(0, N):
    a, b = map(int, input().split())
    if a > b:
        s += b
    else:
        s += a
    if abs(a - b) < c and abs(a - b) % 4 != 0:
        c = abs(a - b)
if c == 300000:
    print("no")
else:
    if s % 4 == 0:
        s += c
    print(s)