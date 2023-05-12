num_list = []
max_index = 0
for i in range(9):
  num_list.append(int(input()))

for i in range(len(num_list)):
  if(num_list[i] == max(num_list)):
    max_index = i + 1

print(max(num_list))
print(max_index)
  
