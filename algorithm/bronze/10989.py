import sys

n = int(input())

count = [0] * 10001

for i in range(n):
  count[int(sys.stdin.readline().strip())] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = '\n')