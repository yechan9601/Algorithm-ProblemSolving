"""
- 홀수이면 안됨
- 처음이 )이면 안됨
- 마지막이 (이면 안됨
"""

def is_vps(string):
  stack = []
  for char in string:
    if char == '(':
      stack.append(char)
    else:
      if not stack: # if ')' and empty
        return False
      stack.pop()
  if stack: # if not empty
    return False
  return True
      

T = int(input())

for i in range(T):
  ps = input()
  if is_vps(ps):
    print('YES')
  else:
    print('NO')
