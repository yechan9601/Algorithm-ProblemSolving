"""
- Enter inputs as start_hr, start_min with map(int, input().split())
- Enter input as duration
- add duration with start_min, then if start_min is over 60, carry
"""

start_hr = 0
start_min = 0

while True:
  start_hr, start_min = map(int, input().split())
  if (start_hr >= 0 or start_hr <= 23 or start_min >= 0 or start_min <= 59):
    break

while True:
  duration = int(input())
  if (duration >= 0 or duration <= 1000):
    break

start_min += duration
start_hr += start_min // 60
start_min %= 60
start_hr %= 24

print(start_hr, start_min)
