"""
3kg, 5kg
GCD: 1 
LCM: 15

정당성: 5kg짜리를 최대한 많이 담아야 봉지의 개수가 적어진다.
5kg로 최대한 나누고, 나머지가 0이 아닐 때 3으로 나누어떨어지지 
않으면 5로 나눈것을 한 번 취소한 뒤 3으로 나눈다. 이후에도
나누어떨어지지 않는다면 -1

"""

n = int(input())

while True:
  bag5 = n // 5
  remaining = n % 5
  if remaining % 3 != 0 and remaining > 0:
    bag5 -= 1
    remaining += 5
  