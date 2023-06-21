import sys

n = int(input())

# d = [0] * (n + 1)
d = []
d.extend([0, 1, 2])

for i in range(len(d), n + 1):
  d.append(d[i - 1] + d[i - 2])

print(d[n] % 10007)