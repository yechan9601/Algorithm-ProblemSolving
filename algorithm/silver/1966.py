"""
input)
T
n idx
array

output) array[idx]가 몇번째로 프린트되는지.
"""
from collections import deque

def printer(queue, target):
  rank = []
  while target in queue:
    isMostImportant = True
    for i in range(1, len(queue)):
      if queue[0][0] < queue[i][0]:
        isMostImportant = False
    if isMostImportant:
      rank.append(queue.popleft())
    else:
      queue.append(queue.popleft())
      isMostImportant = True
  return rank

# main
t = int(input())
for _ in range(t):
  # 입력
  n, idx = map(int, input().split())
  array = list(map(int, input().split()))

  target = [array[idx], idx] # 출력하고자하는 array[i]의 값과 인덱스 저장
  rank = [] # 프린터 출력 중요도 순으로 저장
  queue = deque()
  
  for i in range(len(array)):
    queue.append([array[i], i])
  
  rank = printer(queue, target)

  # 결과 출력
  for i in range(n):
    if target[0] == rank[i][0] and target[1] == rank[i][1]:
      print(i + 1)
      break
  