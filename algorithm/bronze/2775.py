import sys

T = int(input())

for _ in range(T):
  # Enter k n:
  k = int(input()) # k 층
  n = int(input()) # n 호
  # k+1 x n 크기의 2차원 리스트 초기화
  apartment = [[0] * n for _ in range(k+1)]
  
  # 0층 list 생성
  for i in range(1, n + 1):
    apartment[0][i - 1] = i
  
  # k+1 x n 까지의 매트릭스 생성
  for i in range(1, k+1):
    for j in range(n):
      sum = 0
      for q in range(j + 1):
        sum += apartment[i - 1][q]
      apartment[i][j] = sum
  
  print(apartment[k][n-1])
  