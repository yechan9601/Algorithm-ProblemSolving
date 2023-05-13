"""
for char in 'ABC':
  for i in range(3):
    print(char)
"""

num_of_input = int(input())

for i in range(num_of_input):
  R, str = input().split()
  R = int(R)
  # str_to_list = list(str)
  P = []
  for char in str:
    P.append(char * R)
  for result in P:
    print(result, end="")
  print()
