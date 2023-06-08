import sys

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
results = []

for i in range(n):
  for j in range(i + 1, n):
    for q in range(j + 1, n):
      result = cards[i] + cards[j] + cards[q]
      if m >= result:
        results.append(result)

print(max(results))
      


  