"""
input: R1, S (int)

(R1 + R2) / 2 = S
R1 + R2 = 2S
R2 = 2S - R1

output: R2
"""

r1 = 0
s = 0

while True:
  r1, s = input().split()
  if int(r1) >= -1000 and int(r1) <= 1000:
    break
  if int(s) >= -1000 and int(s) <= 1000:
    break

r2 = 2 * int(s) - int(r1)
print(r2)
