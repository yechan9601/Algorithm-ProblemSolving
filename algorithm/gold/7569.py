import sys
input = sys.stdin.readline
from collections import deque

# 입력받기 및 3차원 리스트 초기화
m, n, h = map(int, input().split())
array = []
for i in range(h):
  array.append([list(map(int, input().split())) for _ in range(n)])


# 상 하 좌 우 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# bfs 정의
def bfs():
  # 익은 토마토 찾은 후 모두 큐에 집어넣기
  queue = deque()
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if array[i][j][k] == 1:
          queue.append((i, j, k))
          
  while queue:
    z, x, y = queue.popleft()
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and array[nz][nx][ny] == 0:
        array[nz][nx][ny] = array[z][x][y] + 1
        queue.append((nz, nx, ny))

bfs()
      
days = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if array[i][j][k] == 0:
        print(-1)
        exit()
      days = max(days, array[i][j][k])
print(days - 1)


