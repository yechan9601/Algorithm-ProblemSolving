"""
최대공약수: 유클리드 호제
최소공배수: 두 수를 곱한 값을 최대공약수로 나누기
"""

import sys

x, y = map(int, sys.stdin.readline().split())

def gcd_recursive(a, b):
  if a % b == 0:
    return b
  else:
    return gcd_recursive(b, a % b)

def lcm(a, b):
  return (a * b) // gcd_recursive(a, b)

print(gcd_recursive(x, y))
print(lcm(x, y))
  