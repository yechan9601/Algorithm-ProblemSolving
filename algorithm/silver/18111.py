import sys

def get_minimum_time(array, inventory, min_height, max_height):
  time_list = [] # 특정 높이마다 시간이 얼마나 걸리는지 저장
  min_time = sys.maxsize
  best_height = 0
  for height in range(min_height, max_height + 1): # 중복되지 않는 높이마다
    time = 0
    blocks = inventory
    for ground in array: # array[i][j]마다
      if ground > height:
        time += (ground - height) * 2
        blocks += (ground - height)
      elif ground < height:
        time += (height - ground)
        blocks -= (height - ground)
    if blocks >= 0:
      if time <= min_time:
        min_time = time # update
        best_height = height
  return [min_time, best_height]

# 입력받기
n, m, b = map(int, sys.stdin.readline().split())

array = []
for i in range(n):
  array.extend(list(map(int, sys.stdin.readline().split())))

max_height = max(array)
min_height = min(array)

result = get_minimum_time(array, b, min_height, max_height)
print(f'{result[0]} {result[1]}')
