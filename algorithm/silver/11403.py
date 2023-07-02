import sys
input = sys.stdin.readline

# 노드의 개수 입력받기
n = int(input())

# 그래프의 인접 행렬 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

# 점화식: D[a][b] = min(D[a][b], D[a][k] + D[k][b])
for k in range(n): # 거쳐가는 노드 k
  for a in range(n): 
    for b in range(n):
      # 만약 k를 통해 a로부터 b로 도달할 수 있다면
      if graph[a][k] == 1 and graph[k][b] == 1:
        graph[a][b] = 1
        

for a in range(n):
  for b in range(n):
    if graph[a][b] == 0:
      print(graph[a][b], end = " ")
    else:
      print(1, end = " ")
  print()
