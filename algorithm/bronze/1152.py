str = input().lower()
count = [0] * 26

for c in str:
  if c.isalpha():
    count[ord(c.lower()) - ord('a')] += 1  # ascii code

max_value = max(count)
max_alphabet_list = []

for i in range(len(count)):
  if (max_value == count[i]):
    max_alphabet_list.append(chr(i + ord('a')))

if (len(max_alphabet_list) == 1):
  print(max_alphabet_list[0].upper())
else:
  print("?")
