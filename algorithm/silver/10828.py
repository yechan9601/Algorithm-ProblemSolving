import sys

def push_x(element):
  stack.append(element)

def pop(stack):
  if not stack:
    return -1
  return stack.pop()

def top(stack):
  if not stack:
    return -1
  return stack[-1]


T = int(sys.stdin.readline())

stack = []
for _ in range(T):
  command = sys.stdin.readline().strip()
  # push
  if command[:4] == 'push':
    str, num = command.split(' ')
    push_x(int(num))
  # pop
  if command == 'pop':
    print(pop(stack))
  # size
  if command == 'size':
    print(len(stack))
  # empty
  if command == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  # top
  if command == 'top':
    print(top(stack))