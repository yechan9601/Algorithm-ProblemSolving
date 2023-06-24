import sys
from collections import deque

# 입력받기
m, n = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
  array.append(list(map(int, sys.stdin.readline().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토 좌표 찾기
queue = deque()
for i in range(n):
  for j in range(m):
    if array[i][j] == 1:
      queue.append((i, j))

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어나지 않고, 익지 않은 토마토인 경우
      if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
        array[nx][ny] = array[x][y] + 1
        queue.append((nx, ny)) # 인접한 노드들을 queue에 append

bfs()
  
def check_tomatoes():
    max_day = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                return -1  # 모든 토마토가 익지 못하는 경우
            max_day = max(max_day, array[i][j])
    return max_day - 1  # 첫 번째 날은 1로 시작하므로 1을 빼줌

result = check_tomatoes()
print(result)


  