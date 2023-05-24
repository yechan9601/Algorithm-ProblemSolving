"""
최대 경우의 수: 8
1: U2 L1
2: U2 R1
3: D2 L1
4: D2 R1
5: L2 U1
6: L2 D1
7: R2 U1
8: R2 D1
움직인 좌표는 0보다 크고 8보다 같거나 작으면 됨
"""

coordinate = input()
cnt = 0

col = int(ord(coordinate[0].lower()) - 96)
row = int(coordinate[1])

now = [row, col]

# U D L R
moves = [
  [-2, 0, -1, 0], # d1
  [-2, 0, 0, 1], # d2
  [0, 2, -1, 0], # d3
  [0, 2, 0, 1], # d4
  [-1, 0, -2, 0], # d5
  [0, 1, -2, 0], # d6
  [-1, 0, 0, 2],
  [0, 1, 0, 2]
]

for move in moves:
  dx = move[0] + move[1]
  dy = move[2] + move[3]
  new_move =[now[0] + dx, now[1] + dy]
  if 0 < new_move[0] <= 8 and 0 < new_move[1] <= 8:
    cnt += 1

print(cnt)
   