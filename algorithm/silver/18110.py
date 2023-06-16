import sys
from collections import deque

queue = deque()
trimed_mean = 0.15
array = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
  array.append(int(sys.stdin.readline().rstrip()))

array2 = sorted(array)
for i in range(n):
  queue.append(array2[i])

ignore = int(trimed_mean * float(n) + 0.5)
for i in range(ignore):
  queue.popleft()
  queue.pop()

result = 0.0
if len(queue) > 0:
  result = int(float(sum(queue)) / float(len(queue)) + 0.5)
else:
  result = 0
print(result)