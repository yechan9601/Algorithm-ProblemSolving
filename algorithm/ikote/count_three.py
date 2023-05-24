"""
- N 입력: 00시 00분 00초부터 N시 59분 59초까지 숫자 3이 포함된 시각을 카운트.
ex) N = 1
"""
import sys

N = int(input())

cnt = 0
hours, mins, secs = 0, 0, 0

for hour in range(N + 1):
  for min in range(60):
    for sec in range(60):
      time = str(hour) + ":" + str(min) + ":" + str(sec)
      # if sec % 10 == 0:
      #   print()
      if '3' in time:
        # print('{:>2}:{:>2}:{:>2}'.format(str(hour), str(min), str(sec)), end=' ')
        cnt += 1
    print()
  print()
  print()
  
print(cnt)