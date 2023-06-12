T = int(input())

for _ in range(T):
  h, w, n = map(int, input().split())
  
  floor = n % h
  room = n // h + 1
  if floor == 0: # 만약 나누어떨어지면, 층은 0이 아닌 h, 즉 가장 높은 층
    # 그렇다면 floor 값과 room 값을 조정
    floor = h
    room -= 1

  print(floor * 100 + room)
    
  