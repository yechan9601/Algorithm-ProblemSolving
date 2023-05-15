"""
S = input().lower()

# 1
list = [-1] * 26
for i in range(len(S)) :
  list[ord(S[i]) - ord('a')] = i
"""

S = input().lower()

list = [-1] * 26
for i in range(len(S)) :
  if (list[ord(S[i]) - ord('a')] == -1) : # if the alphabet appears at first time:
    list[ord(S[i]) - ord('a')] = i

for _ in list:
  print(_, end=" ")