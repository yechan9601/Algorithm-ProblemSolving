"""
input: num_of_people (int), size (int), report (list)
print (report[index] - num_of_people * size)
"""

import sys

num_of_people, size = input().split()

result = int(num_of_people) * int(size)

report_input = input().split()
report_list = list(map(int, report_input))

for r in report_list:
  print(r - result, end=" ")
