def isPalindrome(str):
  mid = len(str) // 2
  # 짝수라면
  if len(str) % 2 == 0:
    if str[:mid] == str[-1:mid-1:-1]:
      return 'yes'
  # 홀수라면
  if len(str) % 2 != 0:
    if str[:mid] == str[-1:mid:-1]:
      return 'yes'
  return 'no'

n = 1
while n != 0:
  n = input()
  if n == '0': break
  print(isPalindrome(n))