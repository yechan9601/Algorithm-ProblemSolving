import sys

# Enter how many lines:
lines = int(input())

for i in range(lines):
  # Whitespaces:
  for w in range(lines - i - 1):
    sys.stdout.write(" ")
  # Starts:
  for s in range(i + 1):
    sys.stdout.write("*")
  # New Line:
  sys.stdout.write("\n")
