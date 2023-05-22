"""
정당성 분석:
- 두 숫자에 하나라도 0이 포함되어 있을 때: +
- 두 숫자에 하나라도 1이 포함되어 있을 때 :+
- else: x
"""

s = [int(char) for char in input()]

for i in range(len(s) - 1):
  if s[i] <= 1 or s[i + 1] <= 1:
    s[i + 1] += s[i]
  else:
    s[i + 1] *= s[i]

print(s[len(s) - 1])