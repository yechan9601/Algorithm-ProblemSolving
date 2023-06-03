

n = int(input())

range_start = 2
range_end = range_start + 6 - 1
cnt = 1

while True:
  if n == 1:
    print(1)
    break
  elif range_start <= n <= range_end:
    print(cnt + 1)
    break
  range_start = range_end + 1
  range_end = range_start + 6 * (cnt + 1) - 1
  cnt += 1
