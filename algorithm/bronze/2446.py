"""
1. use double for loop.
2. first for loop: range(N)
3. loop in loop: 
    1) for i in range()
"""

import sys

N = int(input())

for i in range(N - 1):
  for whitespace in range(i):
    sys.stdout.write(" ")
  for star in range(2 * N - (2 * i) - 1):
    sys.stdout.write("*")
  print("")

for i in range(N):
  for whitespace in range(N - i - 1):
    sys.stdout.write(" ")
  for star in range(2 * (i + 1) - 1):
    sys.stdout.write("*")
  print("")
