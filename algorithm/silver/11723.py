import sys
input = sys.stdin.readline

my_set = set([])

m = int(input())
for i in range(m):
  # 입력받기
  command = list(map(str, input().rstrip().split()))
    
  if command[0] == 'add' and int(command[1]) not in my_set:
    my_set.add(int(command[1]))
  elif command[0] == 'remove':
    my_set.discard(int(command[1]))
  elif command[0] == 'check':
    if int(command[1]) in my_set:
      print(1)
    else:
      print(0)
  elif command[0] == 'toggle':
    if int(command[1]) in my_set:
      my_set.remove(int(command[1]))
    else:
      my_set.add(int(command[1]))
  elif command[0] == 'all':
    my_set.update(range(1, 21))
  elif command[0] == 'empty':
    my_set.clear()
    