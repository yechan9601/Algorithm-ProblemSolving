"""
- 공간의 크기 입력받기 (N x N) 2차원 리스트
- 계획서 입력받기
- 시작위치: 1, 1
- 계획서대로 2차원 리스트 상에서 좌표 이동 후 최종 좌표 출력

"""

N = int(input())
plan = input().split()
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
coordinate = [1, 1]

# O(plan)
for direction in plan:
  if direction == 'L' and coordinate[1] + dy[2] > 0:
    coordinate[1] += dy[2]
  if direction == 'R' and coordinate[1] + dy[0] <= N:
    coordinate[1] += dy[0]
  if direction == 'U' and coordinate[0] + dx[1] > 0:
    coordinate[0] += dx[1]
  if direction == 'D' and coordinate[0] + dx[3] <= N:
    coordinate[0] += dx[3]

print(coordinate)




  