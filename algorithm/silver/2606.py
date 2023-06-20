import sys

"""
edge에 기반하여 graph를 재생성하여 dfs/bfs 수행
"""

def dfs(graph, v, visited):
  visited[v] = True
  # print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 입력받기
n = int(input()) # 컴퓨터 수량
num_of_edge = int(input())
edges = []
for i in range(num_of_edge):
  edges.append(list(map(int, sys.stdin.readline().split())))

# edge에 기반하여 graph를 재생성
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
  # i 가 edge[i - 1] ~ 에 있다면 i가 아닌 나머지 숫자를 graph[i]에 append
  for j in range(len(edges)):
    if i in edges[j]:
      graph[i].extend(x for x in edges[j] if x != i)

# 결과 출력
visited = [False] * (n + 1)
dfs(graph, 1, visited)
cnt = 0
for visit in visited:
  if visit == True:
    cnt += 1
print(cnt - 1)



      
