import sys
input = sys.stdin.readline

# 주어진 2차원 배열에서 모두가 같은 색인지 확인하는 메서드
def check_color(array, x, y, n):
  color = array[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if array[i][j] != color:
        return False
  return True

# def divide_paper(배열, x좌표, y좌표, 색종이너비, 흰색 및 파란색 종이 개수)
def divide_paper(array, x, y, n, count):
  if check_color(array, x, y, n): # 만약 모두 같은 색이면
    if array[x][y] == 0:
      count[0] += 1
    else:
      count[1] += 1
  else: # 만약 모두 같은 색이 아니라면
    m = n // 2 # update mid
    # 4사분면 탐색
    divide_paper(array, x, y, m, count)
    divide_paper(array, x, y + m, m, count)
    divide_paper(array, x + m, y, m, count)
    divide_paper(array, x + m, y + m, m, count)


# 입력받기
n = int(input())
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

count = [0, 0] # 흰색, 파란색 종이 카운트
divide_paper(array, 0, 0, n, count)

# Print Result
print(count[0])
print(count[1])