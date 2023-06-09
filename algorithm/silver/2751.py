import sys

n = int(sys.stdin.readline().strip())

array = []
for _ in range(n):
  array.append(int(sys.stdin.readline().strip()))

array.sort()
for _ in range(n):
  print(array[_])