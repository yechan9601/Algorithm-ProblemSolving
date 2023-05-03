"""
1. String input, list reverse_str
2. for loop, append 
"""

str = ""
reverse_str = []

while (str != "END"):
  try:
    str = input()
    if(str == "END"):
      break;
    else:
      # reverse the string.
      reverse = str[::-1]
      reverse_str.append(reverse)
  except ExceptionType:
    print(ExceptionType)
  

for encoded_str in reverse_str:
  print(encoded_str, end="\n")

