"""
문제해결 아이디어: 
최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 주면 됨

정당성 분석: 
가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 
작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문.
(만약 800원을 거슬러 주어야 하는데 화폐 단위가 500, 400, 100원이라면?)
"""

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
  count += n // coin
  n %= coin

print(count)

# 화폐의 종류가 K라고 할 때, 시간복잡도는 O(K)
