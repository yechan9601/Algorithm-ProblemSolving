import sys

n = int(sys.stdin.readline().rstrip())

d = [0, 1, 3]

if n <= 2:
  print(d[n] % 10007)
else:
  for i in range(3, n + 1):
    d.append(d[i - 1] + d[i - 2] * 2)
  print(d[n] % 10007)