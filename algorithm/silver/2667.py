import sys
from collections import deque

# 입력받기
n = int(input())
array = []
for i in range(n):
  array.append(list(map(str, sys.stdin.readline().rstrip())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
danji = []

# 단지번호를 매기고 단지마다의 집 개수를 카운트하는 bfs 함수
def bfs(x, y, danji_no):
  queue = deque()
  queue.append((x, y)) # x, y좌표를 튜플로 큐에 추가
  array[x][y] = danji_no
  cnt = 1
  while queue: # 큐가 빌때까지
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n: # 만약 2차원 리스트의 범위를 벗어나면
        continue
      if array[nx][ny] != '1':
        continue
      if array[nx][ny] == '1':
        array[nx][ny] = danji_no
        queue.append((nx, ny))
        cnt += 1
  danji.append(cnt)

# bfs 실행
danji_no = 1
for i in range(n):
  for j in range(n):
    if array[i][j] == '1':
      bfs(i, j, danji_no)
      danji_no += 1
      
# 결과출력
print(len(danji))
for houses in sorted(danji):
  print(houses)