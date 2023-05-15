ABC = [int(input()) for _ in range(3)]

result = ABC[0] * ABC[1] * ABC[2]

result = str(result)

count = [0] * 10
for num in result :
  count[int(num)] += 1

for i in range(len(count)) :
  print(count[i])
  