import sys

dp = [(1, 0), (0, 1)]
def cnt_fibo(x):
  # 테스트 케이스로 여러번 중복될 것을 예상:
  if len(dp) > x:
    return dp[x]
  for i in range(len(dp), x + 1):
    dp.append((dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]))
  return dp[x]

# 입력받기
t = int(input())

for i in range(t):
  n = int(input())
  cnt0, cnt1 = cnt_fibo(n)
  print(cnt0, cnt1)