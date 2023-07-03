import sys
input = sys.stdin.readline

"""
알몸이 아닌 상태로 의상을 입을 수 있는 경우: 
(a종류의 개수 + 1) * (b종류의 개수 + 1) * ... * (z 종류의 개수 + 1) - 1
"""

# main
T = int(input())

# Test case
for _ in range(T):
  # n의 개수 입력받기
  n = int(input())
  fashion = {}
  # 패션 이름, 종류 입력받기
  for i in range(n):
    name, category = map(str, input().split())
    if category in fashion.keys():
      fashion[category].append(name)
    else:
      fashion[category] = [name]
  # 중복 갯수 계산하기
  result = 1
  for j in fashion.keys():
    result *= (len(fashion[j]) + 1)
  print(result - 1)