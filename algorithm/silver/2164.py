import sys
from collections import deque

queue = deque()

n = int(input())

# n만큼 큐에 저장
for i in range(n):
  queue.append(i + 1)

# 한장이 남을때까지:
while len(queue) > 1:
  queue.popleft()
  if len(queue) < 1:
    break
  queue.append(queue.popleft())

# 마지막 남게 되는 카드 출력
if queue:
  print(queue[0])

  