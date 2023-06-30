import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

sum_list = []
max_sum = 0
# Up Down Left Right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def tetromino1(array, x, y):
  # z : last coordinate of tetromino
  zy = y + 3
  if 0 <= zy < m:
    sum_list.append(sum(array[x][y : zy + 1]))
  zx = x + 3
  if 0 <= zx < n:
    sum_list.append(sum(row[y] for row in array[x : zx + 1]))

def tetromino2(array, x, y):
  if 0 <= x + 1 < n and 0 <= y + 1 < m:
    tetromino = [row[y : y + 2] for row in array[x : x + 2]]
    total = 0
    for row in tetromino:
      for col in row:
        total += col
    sum_list.append(total)

def tetromino3(array, x, y):
  # UU L/R
  if 0 <= x - 2 < n and 0 <= y - 1 < m:
    sum_list.append(array[x][y] + array[x - 1][y] + array[x - 2][y] + array[x - 2][y - 1])
  if 0 <= x - 2 < n and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x - 1][y] + array[x - 2][y] + array[x - 2][y + 1])
  
  # DD L/R
  if 0 <= x + 2 < n and 0 <= y - 1 < m:
    sum_list.append(array[x][y] + array[x + 1][y] + array[x + 2][y] + array[x + 2][y - 1])
  if 0 <= x + 2 < n and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x + 1][y] + array[x + 2][y] + array[x + 2][y + 1])

  # LL U/D
  if 0 <= x - 1 < n and 0 <= y - 2 < m:
    sum_list.append(array[x][y] + array[x][y - 1] + array[x][y - 2] + array[x - 1][y - 2])
  if 0 <= x + 1 < n and 0 <= y - 2 < m:
    sum_list.append(array[x][y] + array[x][y - 1] + array[x][y - 2] + array[x + 1][y - 2])

  # RR U/D
  if 0 <= x - 1 < n and 0 <= y + 2 < m:
    sum_list.append(array[x][y] + array[x][y + 1] + array[x][y + 2] + array[x - 1][y + 2])
  if 0 <= x + 1 < n and 0 <= y + 2 < m:
    sum_list.append(array[x][y] + array[x][y + 1] + array[x][y + 2] + array[x + 1][y + 2])

def tetromino4(array, x, y):
  if 0 <= x + 2 < n and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x + 1][y] + array[x + 1][y + 1] + array[x + 2][y + 1])
  if 0 <= x + 2 < n and 0 <= y - 1 < m:
    sum_list.append(array[x][y] + array[x + 1][y] + array[x + 1][y - 1] + array[x + 2][y - 1])
  if 0 <= x - 1 < n and 0 <= y + 2 < m:
    sum_list.append(array[x][y] + array[x][y + 1] + array[x - 1][y + 1] + array[x - 1][y + 2])
  if 0 <= x - 1 < n and 0 <= y - 2 < m:
    sum_list.append(array[x][y] + array[x][y - 1] + array[x - 1][y - 1] + array[x - 1][y - 2])
  if 0 <= x + 1 < n and 0 <= y + 2 < m:
    sum_list.append(array[x][y] + array[x][y + 1] + array[x + 1][y + 1] + array[x + 1][y + 2])
  if 0 <= x + 1 < n and 0 <= y - 2 < m:
    sum_list.append(array[x][y] + array[x][y - 1] + array[x + 1][y - 1] + array[x + 1][y - 2])
  if 0 <= x - 2 < n and 0 <= y - 1 < m:
    sum_list.append(array[x][y] + array[x - 1][y] + array[x - 1][y - 1] + array[x - 2][y - 1])
  if 0 <= x - 2 < n and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x - 1][y] + array[x - 1][y + 1] + array[x - 2][y + 1])
  
def tetromino5(array, x, y):
  if 0 <= x - 1 < n and 0 <= y - 1 < m and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x - 1][y] + array[x][y - 1] + array[x][y + 1])
  if 0 <= x + 1 < n and 0 <= y - 1 < m and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x + 1][y] + array[x][y - 1] + array[x][y + 1])
  if 0 <= x - 1 < n and 0 <= x + 1 < n and 0 <= y + 1 < m:
    sum_list.append(array[x][y] + array[x][y + 1] + array[x - 1][y] + array[x + 1][y])
  if 0 <= x - 1 < n and 0 <= x + 1 < n and 0 <= y - 1 < m:
    sum_list.append(array[x][y] + array[x][y - 1] + array[x - 1][y] + array[x + 1][y])
  

for i in range(n):
  for j in range(m):
    tetromino1(array, i, j)
    tetromino2(array, i, j)
    tetromino3(array, i, j)
    tetromino4(array, i, j)
    tetromino5(array, i, j)

# 결과 출력
if sum_list:
  max_sum = max(sum_list)
print(max_sum)