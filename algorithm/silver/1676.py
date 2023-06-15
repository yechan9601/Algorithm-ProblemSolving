def factorial(x):
  if x == 0 or x == 1:
    return 1
  return x * factorial(x - 1)

# N!의 뒤에서부터 0이 아닌 숫자가 나올때까지의 0의 개수를 리턴하는 함수
def count_zero_back(str):
  cnt = 0
  for i in range(len(str)-1, -1, -1):
    if str[i] != '0':
      break
    cnt += 1
  return cnt
  

n = int(input())
print(count_zero_back(str(factorial(n))))
