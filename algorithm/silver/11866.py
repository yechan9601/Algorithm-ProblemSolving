n, k = map(int, input().split())

array = []
for i in range(1, n + 1):
  array.append(i)

i = k - 1
temp = []
while len(array) > 0:
  if i <= len(array) - 1:
    temp.append(array[i])
    array.remove(array[i])
    i += (k - 1)
  else:
      i -= len(array)

result = ', '.join(map(str, temp))
print(f'<{result}>')