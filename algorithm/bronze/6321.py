# 파이썬에서 아스키코드 활용방법:
# char = 'A'
# ascii_code = ord(char)
# print(ascii_code)
# print(chr(ascii_code))

# Enter How many inputs?:
N = int(input())

# Enter names:
names = []
for i in range(N):
  str = input()
  # Change Strings
  new_str = ""
  for q in range(len(str)):
    ascii_code = ord(str[q])
    if (ascii_code == 90):
      ascii_code -= 26
    new_str += chr(ascii_code + 1)

  names.append(new_str)

# Print results:
for w in range(len(names)):
  print("String #{}\n{}\n".format(w + 1, names[w]))
