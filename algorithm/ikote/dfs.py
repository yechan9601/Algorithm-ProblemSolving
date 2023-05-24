# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],  # 그래프에선 보편적으로 0이 아닌 1부터 시작하기 때문에 graph[0] 비워두기.
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:  # 종료조건
      dfs(graph, i, visited)


# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)
