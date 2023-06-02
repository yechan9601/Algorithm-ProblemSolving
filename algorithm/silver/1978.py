"""
주어진 수 N개 중에서 소수가 몇개인지 세는 프로그램.
소수란? 1 또는 자기 자신으로만 나누어떨어지는 숫자. 1, 2, 3, 5, 7, 11... 

에라토스테네스 알고리즘?
"""

n = int(input())

numbers = list(map(int, input().split()))
cnt = 0

for num in numbers:
  if num == 1:
    continue
  cnt += 1
  for j in range(2, num - 1):
    if num % j == 0: # 한 번이라도 나누어 떨어진다면:
      cnt -= 1
      break

print(cnt)