import sys
from collections import deque

class Queue:
  def __init__(self):
    self.queue = []

  def push_front(self, x):
    temp = []
    for element in self.queue:
      temp.append(element)
    self.queue.clear()
    self.queue.append(x)
    for element in temp:
      self.queue.append(element)

  def push_back(self, x):
    self.queue.append(x)

  def pop_front(self):
    if self.queue:
      temp = []
      front = self.queue[0]
      for i in range(1, len(self.queue)):
        temp.append(self.queue[i])
      self.queue.clear()
      for element in temp:
        self.queue.append(element)
      return front
    else:
      return -1

  def pop_back(self):
    if self.queue:
      return self.queue.pop()
    else: 
      return -1

  def size(self):
    return len(self.queue)

  def empty(self):
    if self.queue:
      return 0
    else: return 1

  def front(self):
    if self.queue:
      return self.queue[0]
    else: return -1

  def back(self):
    if self.queue:
      return self.queue[-1]
    else: return -1

n = int(input())

queue = Queue()

for _ in range(n):
  command = sys.stdin.readline().rsplit()
  if command[0] == 'push_front':
    queue.push_front(int(command[1]))
  elif command[0] == 'push_back':
    queue.push_back(int(command[1]))
  elif command[0] == 'pop_front':
    print(queue.pop_front())
  elif command[0] == 'pop_back':
    print(queue.pop_back())
  elif command[0] == 'size':
    print(queue.size())
  elif command[0] == 'empty':
    print(queue.empty())
  elif command[0] == 'front':
    print(queue.front())
  elif command[0] == 'back':
    print(queue.back())
  