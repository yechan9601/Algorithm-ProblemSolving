import sys

# Enter how many lines:
lines = int(input())

# Print
for i in range(lines):
  # Print stars:
  for s in range(lines - i):
    sys.stdout.write("*")
  # Print new line:
  print("")