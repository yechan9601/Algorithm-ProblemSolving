"""
X사를 골랐을 때 요금: A * P
Y사를 골랐을 때 요금: B + (P - C) * D

var: 
  inputs: A, B, C, D, P
  X, Y
"""

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P

if (P < C):
  Y = B
else:
  Y = B + (P - C) * D

if (X < Y):
  print(X)
else:
  print(Y)
