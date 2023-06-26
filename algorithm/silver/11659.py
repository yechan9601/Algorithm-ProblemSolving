import sys

# 입력받기
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# dp 처럼 누적합 생성
sum_cumulated = [0]
for i in range(1, len(numbers) + 1):
  sum_cumulated.append(sum_cumulated[i - 1] + numbers[i - 1])

# 범위 (i, j) 입력받은 뒤, 결과 출력
for x in range(m):
  i, j = map(int, sys.stdin.readline().split())
  result = sum_cumulated[j] - sum_cumulated[i - 1]
  print(result)

