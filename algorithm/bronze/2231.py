import sys

def get_digit_sum(x):
  array = []
  for digit in str(x):
    array.append(int(digit))
  return sum(array)
    
# 숫자 n 입력
n = sys.stdin.readline().strip()
n = int(n)
for i in range(n):
  result = i + get_digit_sum(i)
  if result == n:
    print(i)
    break
  if i == n - 1:
    print(0)
