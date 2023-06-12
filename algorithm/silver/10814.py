n = int(input())

users = []
for i in range(n):
  age, name = map(str, input().split())
  users.append([int(age), name])

users.sort(key = lambda x : x[0])

for i in range(n):
  print(users[i][0], users[i][1])
  