import heapq
import sys
input = sys.stdin.readline


def abs_key(x):
  return abs(x)
  
n = int(input())
h = []
for _ in range(n):
  num = int(input())
  # 값이 0이 아닐때
  if num != 0:
    heapq.heappush(h, (abs(num), num))
  # 값이 0일때
  else:
    # 힙이 비어있을 때
    if not h:
      print(0)
    else:
      print(heapq.heappop(h)[1])
      

    
    
  