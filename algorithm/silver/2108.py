import sys
from collections import Counter

def avg(array):
  total = sum(array)
  total = float(total)
  result = round(total / len(array))
  return int(result)

def mid(array):
  array.sort()
  return array[len(array) // 2]

def most_frequent(array):
  counter = Counter(array)
  max_frequency = max(counter.values()) # 최대 빈도 횟수
  # print(f'max frequency is... {max_frequency}')
  # 최대 빈도와 같은 빈도를 가지는 요소들을 찾습니다.
  most_common = [element for element, frequency in counter.items() 
                 if frequency == max_frequency]
  most_common.sort()
  if len(most_common) < 2:
    return most_common[0]
  else:
    return most_common[1]

def get_range(array):
  return max(array) - min(array)
  
  

n = int(input())
array = []
for i in range(n):
  array.append(int(sys.stdin.readline().rstrip()))

print(avg(array))
print(mid(array))
print(most_frequent(array))
print(get_range(array))

