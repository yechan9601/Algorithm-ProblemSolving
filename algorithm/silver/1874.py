import sys

n = int(input())
array = []
array2 = []
for i in range(n):
  array.append(int(input()))

# 스택에 오름차순으로 넣기 위한 임시 리스트
descending = []
for i in range(n, 0, -1):
  descending.append(i)
  
stack = []
calculations = []

# 수열의 숫자순서대로 탐색하여 push & pop
for num in array:
  # 스택이 비어있는 경우: 찾는 숫자가 스택의 맨뒤에 올때까지 push한뒤 pop
  if not stack:
    while descending:
      stack.append(descending.pop())
      calculations.append('+')
      if stack[-1] == num: 
        array2.append(stack.pop())
        calculations.append('-')
        break
      
  # 스택이 안 비어있는 경우
  else:
    # 맨뒤 요소가 찾는 수열의 숫자가 아닐때: 찾는 숫자가 스택의 맨뒤에 올때까지 push한뒤 pop
    if stack[-1] != num:
      while descending:
        stack.append(descending.pop())
        calculations.append('+')
        if stack[-1] == num:
          array2.append(stack.pop())
          calculations.append('-')
          break
        
    # 맨뒤 요소가 찾는 수열의 숫자일때: 바로 pop
    else:
      array2.append(stack.pop())
      calculations.append('-')
  
# print(f'array: {array}')
# print(f'array2: {array2}')
# print(f'calculations: {calculations}')
if array == array2:
  for cal in calculations:
    print(cal)
    
else:
  print('NO')

