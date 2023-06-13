from collections import Counter
import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(sys.stdin.readline().split())

counter = Counter(n_list)

for m in m_list:
  print(counter[int(m)], end=' ')
