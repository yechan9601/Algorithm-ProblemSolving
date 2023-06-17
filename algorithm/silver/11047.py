"""
Greedy: 
  정당성 분석: 
    "k에 대하여, 큰 화폐 단위로 나눌 수록 동전의 개수를 최소화시킬 수 있다."

DP:
  1 <= K <= 100,000,000 이므로 메모리 초과!
"""

import sys

# n, k = map(int, sys.stdin.readline().split())

# d = [k + 1] * (k + 1)
# d[0] = 0

# currency = []
# for i in range(n):
#   currency.append(int(sys.stdin.readline().rstrip()))

# for i in range(n): # 각 화폐의 단위마다
#   for j in range(currency[i], k + 1): # 화폐의 금액부터 목표 금액까지의 범위
#     d[j] = min(d[j], d[j - currency[i]] + 1)

# print(d[k])

n, k = map(int, sys.stdin.readline().split())

currency = []
for i in range(n):
  currency.append(int(sys.stdin.readline().rstrip()))

result = 0
for i in range(n-1, -1, -1):
  if currency[i] <= k:
    result += k // currency[i]
    k = k % currency[i]

print(result)



