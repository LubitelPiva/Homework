N = int(input())
b = ""
maxx = 0
one = ""
for i in range(1, N + 1):
  a = float(input())
  if a > float(1):
    b += str(i) + ' '
  elif a == float(1):
    one += i + ' '
  elif a > maxx:
    maxx = i
if len(b) != 0:
  print(b)
elif len(one) != 0:
  print(one)
else:
  print(maxx)