"""
input)
13
0
1
2
0
0
3
2
1
0
0
0
0
0
output)
0
2
1
3
2
1
0
0
"""

import sys
input = sys.stdin.readline
import heapq

h = []
n = int(input())
for i in range(n):
  num = int(input())
  if num != 0:
    heapq.heappush(h, -num)
  else:
    if h:
      print(-heapq.heappop(h))
    else:
      print(0)