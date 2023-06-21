import sys

# 입력받기
n = int(input())
array = [0] * (n + 1)
for i in range(1, n + 1):
  array[i] = int(input())
  
# DP Table 생성
d = [0] * (n + 1)
if n == 1:
  d[n] = array[n]
elif n == 2:
  d[n] = array[n - 1] + array[n]
else:
  d[1] = array[1]
  d[2] = array[1] + array[2]
  d[3] = max(array[2] + d[0], d[1]) + array[3]

# Dynamic Programming (bottom up)
for i in range(4, len(d)):
  d[i] = max(array[i - 1] + d[i - 3], d[i - 2]) + array[i]

# 결과출력
print(d[n])