from collections import deque
import sys

def push_X(queue, x):
  queue.append(x)

def pop(queue):
  if queue:
    return queue.popleft()
  else:
    return -1

def size(queue):
  return len(queue)

def empty(queue):
  if queue:
    return 0
  else:
    return 1

def front(queue):
  if queue:
    print(queue[0])
  else:
    print(-1)

def back(queue):
  if queue:
    print(queue[-1])
  else:
    print(-1)
  

queue = deque()

n = int(input())

for _ in range(n):
  command = sys.stdin.readline().strip()
  if 'push' in command:
    str, num = command.split()
    push_X(queue, num)
  elif command == 'pop':
    print(pop(queue))
  elif command == 'size':
    print(size(queue))
  elif command == 'empty':
    print(empty(queue))
  elif command == 'front':
    front(queue)
  elif command == 'back':
    back(queue)