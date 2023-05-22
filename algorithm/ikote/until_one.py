"""
문제해결 아이디어:
최대한 많이 나누기를 수행

정당성 분석:
N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있다.
K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있습니다.
"""

# O(n)
n, k = map(int, input().split())

cnt = 0

while n != 1:
  if n % k == 0:
    n //= k
  else:
    n -= 1
  cnt += 1

print(cnt)

# O(logN)
n, k = map(int, input().split())  # ex) 25 3

result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n // k) * k  # 가장 가까운 나누어떨어지는 숫자 target
  result += (n - target)  # ex) target까지 뺄셈을 진행한 횟수
  n = target  # 횟수를 올려주었으니 n은 타겟 숫자가 됨

  # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break

  # K로 나누기
  result += 1  # 나눗셈 진행하므로 횟수 1 추가
  n //= k

# 더이상 나누기를 할 수 없는 수에 대하여 1씩 뺀 횟수를 추가
result += (n - 1)
print(result)
