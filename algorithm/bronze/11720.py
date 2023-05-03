"""
1. int num_of_input, String num_str
"""
num_of_input = 0
num_str = ""
total = 0

num_of_input = int(input())

num_str = input()

for i in range(len(num_str)):
  total += int(num_str[i])

print(total)
  