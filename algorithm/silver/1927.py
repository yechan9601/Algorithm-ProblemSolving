"""
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. x는 231보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.
input)
9
0
12345678
1
2
0
0
0
0
32

output)
0
1
2
12345678
0
"""

import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
h = []
result = []
for i in range(n):
  num = int(input().rstrip())
  if num!= 0:
    # heappush(list, value)
    heapq.heappush(h, num)
  else:
    # print and heappop(list)
    if h:
      print(heapq.heappop(h))
    else:
      print(0)
