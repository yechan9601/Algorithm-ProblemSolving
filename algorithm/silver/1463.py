"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

점화식:
a[i] : x를 3가지 연산을 활용하여 1로 만드는 최소횟수
a[i] = min(a[i//3], a[i//2]) + 1
"""

x = int(input())

d = [0] * (x + 1)

for i in range(2, x + 1):
  # -1 계산
  d[i] = d[i - 1] + 1
  # 나누기 2 계산
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  # 나누기 3 계산
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)

print(d[x])
