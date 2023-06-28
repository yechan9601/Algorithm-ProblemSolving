import sys
input = sys.stdin.readline
from collections import deque

# 2의 위치 찾는 메서드
def find_destination(array):
  for i in range(len(array)):
    for j in range(len(array[i])):
      if array[i][j] == 2:
        return (i, j)

# 입력받기
n, m = map(int, input().split())
array = []
result = [[0] * m for _ in range(n)]
for i in range(n):
  array.append(list(map(int, input().split())))
  
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 메서드
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      elif array[nx][ny] == 0:
        continue
      elif array[nx][ny] == 1:
        array[nx][ny] = array[x][y] + 1
        result[nx][ny] = result[x][y] + 1
        queue.append((nx, ny))

# 2의 좌표 찿기 및 bfs 실행
a, b = find_destination(array)
bfs(a, b)

# 땅이 1인 부분 중 도달할 수 없는 위치는 -1
for i in range(len(array)):
  for j in range(len(array[i])):
    if array[i][j] == 1:
      result[i][j] = -1

for row in result:
  for col in row:
    print(col, end = ' ')
  print()

