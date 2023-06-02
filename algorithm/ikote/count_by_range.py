n, x = map(int, input().split())

array = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count_by_range(list, left, right):
  r_idx = bisect_right(list, right)
  l_idx = bisect_left(list, left)
  return r_idx - l_idx

print(count_by_range(array, x, x))