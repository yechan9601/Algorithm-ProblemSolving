import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# target == mid일 수 없을 때가 있으므로, 가장 가까운 값을 찾기 위해선 재귀함수가 아닌 while로 대체.
def binary_search(array, target, start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    remainders = sum([num - mid for num in array if num > mid]) # 자른 나무들의 합
    if remainders < target: # 왼쪽 탐색
      end = mid - 1
    if remainders >= target: # 오른쪽 탐색
      result = mid
      start = mid + 1
  return result

max_value = max(array)
print(binary_search(array, m, 0, max_value))