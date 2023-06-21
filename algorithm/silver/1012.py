import sys
from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
group = []

def solution(x, y, num):
  queue = deque()
  queue.append((x, y))
  array[x][y] = num
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny >= m or nx < 0 or nx >= n:
        continue
      if array[nx][ny] == '0':
        continue
      if array[nx][ny] == '1':
        array[nx][ny] = num
        queue.append((nx, ny))
  group.append(num)

for i in range(int(input())): # testcases
  # 입력받기
  m, n, k = map(int, sys.stdin.readline().split())
  # 2차원 배열 생성
  array = [['0'] * m for _ in range(n)]
  for j in range(k):
    y, x = map(int, sys.stdin.readline().split())
    array[x][y] = '1'
  # bfs 실행
  group_no = 1
  for p in range(n):
    for q in range(m):
      if array[p][q] == '1':
        solution(p, q, group_no)
        group_no += 1
  # 결과 출력
  print(len(group))
  group.clear()
  
  
  

  