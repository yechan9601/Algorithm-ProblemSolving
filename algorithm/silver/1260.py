"""
번호가 낮은 인접노드부터의 탐색 순서 : 
stack:
[1
[1, 2
[1, 2, 7
[1, 2, 7, 6
# (pop 6) [1, 2, 7
[1, 2, 7, 8
# (pop 8) [1, 2, 7
# (pop 7) [1, 2
# (pop 2) [1
[1, 3
[1, 3, 4
[1, 3, 4, 5
# (pop 5) [1, 3, 4
# (pop 4) [1, 3
# (pop 3) [1
# (pop 1) 

1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5
"""

import sys
from collections import deque

def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  for i in sorted(graph[v]):
    if not visited[i]:  # 종료조건
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 활용
  queue = deque([start])
  # 현재 노드를 방문처리
  visited[start] = True
  print(start, end = ' ')
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    # print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in sorted(graph[v]):
      if not visited[i]:
        queue.append(i)
        print(i, end = ' ')
        visited[i] = True

# 입력받기
n, m, v = map(int, sys.stdin.readline().split())
array = []
for i in range(m):
  array.append(list(map(int, sys.stdin.readline().split())))

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
  for j in range(m):
    if i in array[j]:
      graph[i].extend(x for x in array[j] if x != i)

# print(graph)

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)