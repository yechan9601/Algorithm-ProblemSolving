import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(array, x, y, is_blind):
  queue = deque([(x, y)])
  color = array[x][y]
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 다음 위치가 범위 내인 경우
      if 0 <= nx < n and 0 <= ny < n:
        # 적록색약인 경우
        if is_blind:
          if color == 'R' or color == 'G':
            if array[nx][ny] == 'R' or array[nx][ny] == 'G':
              if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
          else:
            if array[nx][ny] == 'B':
              if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
        # 적록색약이 아닌 경우
        else:
          if array[nx][ny] == color:
            if not visited[nx][ny]:
              visited[nx][ny] = True
              queue.append((nx, ny))

def count_areas(array, is_blind):
  count = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        bfs(array, i, j, is_blind)
        count += 1
  return count

# 입력받기
n = int(input())
array = []
for i in range(n):
  array.append(list(input().rstrip()))
visited = [[False] * n for _ in range(n)]

# bfs 실행
count_normal = count_areas(array, False)
visited = [[False] * n for _ in range(n)] # is_blind = True로 한번 더 진행하기 위해 visited 다시 초기화
# 모든 R을 G로 변환
for i in range(n):
  for j in range(n):
    if array[i][j] == 'R':
      array[i][j] = 'G'
count_blind = count_areas(array, True)

# 결과 출력
print(count_normal, count_blind)