import sys

def check_triangle(a, b, c):
  if a == max(a, b, c):
    if a*a == b*b + c*c:
      return 'right'
  elif b == max(a, b, c):
    if b*b == a*a + c*c:
      return 'right'
  elif c == max(a, b, c):
    if c*c == b*b + a*a:
      return 'right'
  return 'wrong'

a, b, c = 1, 1, 1
while a + b + c != 0:
  a, b, c = map(int, sys.stdin.readline().split())
  if a + b + c == 0:
    break
  print(check_triangle(a, b, c))