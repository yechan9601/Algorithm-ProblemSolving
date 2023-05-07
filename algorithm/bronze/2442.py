import sys

N = int(input())

for i in range(N):
  # whitespaces:
  for w in range(N - i - 1):
    sys.stdout.write(" ")
  # stars:
  for s in range(2 * (i + 1) - 1):
    sys.stdout.write("*")
  sys.stdout.write("\n")