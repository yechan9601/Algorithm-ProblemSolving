import sys
input = sys.stdin.readline

def possible(channel, broken):
  channel = str(channel)
  for digit in channel:
    if digit in broken:
      return False
  return True

def count_press(channel, broken):
  if channel == 100:
    return 0
  min_press = abs(channel - 100)
  for i in range(1000001):
    if possible(i, broken):
      # 현재채널의 버튼횟수 + (목표채널 - 현재채널)
      min_press = min(len(str(i)) + abs(i - channel), min_press)
  return min_press

# main
n = int(input())
m = int(input())

if m > 0:
  broken = input().split()
else:
  broken = []

result = count_press(n, broken)
print(result)