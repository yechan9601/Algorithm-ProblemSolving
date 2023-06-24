import sys
from collections import deque

# 입력받기
node, edge = map(int, sys.stdin.readline().split())
array = []
for i in range(edge):
  a, b = map(int, sys.stdin.readline().split())
  array.append((a, b))

# 그래프 재생성
def adjacent_graph(edges):
  graph = [[] for _ in range(node + 1)]
  graph[0].append(0)
  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
  return graph

adjacent_list = adjacent_graph(array)

# bfs
def bfs(graph, start, visited, cnt):
  queue = deque()
  queue.append(start)
  visited[start] = cnt
  while queue:
    v = queue.popleft()
    # print(v, end = ' ')
    for i in graph[v]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = cnt

visited = [0] * (node + 1)
cnt = 1
for i in range(1, node + 1):
  if visited[i] == 0:
    bfs(adjacent_list, i, visited, cnt)
    cnt += 1

# 결과 출력
print(max(visited))
