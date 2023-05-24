def dfs(x, y):
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y) # up
    dfs(x + 1, y) # down
    dfs(x, y - 1) # left
    dfs(x, y + 1) # right
    return True
  return False
  
N, M = map(int, input().split())
cnt = 0
graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      cnt += 1

print(cnt)


  




# def dfs(graph, v, visited):
#   # 현재 노드를 방문처리
#   visited[v] = True
#   print(v, end=' ')
#   for i in graph[v]:
#     if not visited[i]:  # 종료조건
#       dfs(graph, i, visited)
