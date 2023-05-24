"""
<ascii code Char to Dec>
- char 0부터 9는 ascii code Dec: 48 ~ 57
- char 대문자 알파벳은 ascii code Dec: 65 ~ 90
- char 소문자 알파벳은 ascii code Dec: 97 ~ 122
"""

str1 = input()
result = []
num = 0

for char in str1:
  if 65 <= ord(char) <= 90:  # Upper case char ascii code
    result.append(char)
  elif 48 <= ord(char) <= 57:  # 0~9 char ascii code
    num += int(char)

result.sort()
num_str = str(num)

print('{}{}'.format(''.join(result), num_str))
