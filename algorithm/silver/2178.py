from collections import deque
import sys

# 입력받기
n, m = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
  array.append(list(map(int, sys.stdin.readline().rstrip())))
  
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4): # 인접한 노드들을 모두 방문하기 위해
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어나는 경우
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 다음 좌표의 값이 0인 경우
      if array[nx][ny] == 0:
        continue
      if array[nx][ny] == 1:
        array[nx][ny] = array[x][y] + 1
        queue.append((nx, ny))
  return array[n - 1][m - 1]
      
print(bfs(0, 0))
