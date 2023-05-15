"""
1. dict?
2. set? (중복 값 없음)
3. list? (중복 값 있음)
"""

remainder = set()  # set

for i in range(10):
  num = int(input())
  remainder.add(num % 42)

print(len(remainder))
