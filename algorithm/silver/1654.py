import sys

def cut_lanport_max(start, end, array, target):
  result = 0
  while start <= end:
    total = 0
    mid = (start + end) // 2
    # 잘랐을 때 랜선 개수 계산
    for x in array:
      if x >= mid:
        total += (x // mid)
    if total < target:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
  return result

n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(sys.stdin.readline().rstrip()))

print(cut_lanport_max(1, max(array), array, m))
