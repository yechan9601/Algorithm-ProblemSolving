"""
ord('a') : 97
ord('A') : 65
"""

import sys

def hashing(l, str, m):
  total = 0
  for i in range(l):
    result = (ord(str[i]) - 96) * (31 ** i)
    total += result
  return total % m
      
  
l = int(input())
string1 = sys.stdin.readline().rstrip().lower()
m = 1234567891

print(hashing(l, string1, m))
