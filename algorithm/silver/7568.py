import sys

n = int(input())
sizes = []

for i in range(n):
  w, h = map(int, sys.stdin.readline().split())
  sizes.append([w, h])

rank_list = []
for i in range(len(sizes)):
  rank = 0
  for j in range(len(sizes)):
    if i != j:
      if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]:
        rank += 1
    else:
      continue
  rank_list.append(rank + 1)

for i in range(n):
  print(rank_list[i], end=' ')