"""
정당성 분석: p를 정렬하고 i번째까지의 합을 리스트에 추가. 리스트 요소들의 총합은 항상 최소이다. 
"""

import sys

n = int(input())
p = list(map(int, sys.stdin.readline().split()))

# p = sorted(p)
p.sort()
result = []
for i in range(n):
  cumulated = 0
  for j in range(i + 1):
    # i번째까지의 합
    cumulated += p[j]
  result.append(cumulated)

print(sum(result))