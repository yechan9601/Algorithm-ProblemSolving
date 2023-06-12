import sys

# 이진 탐색 함수
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif target < array[mid]:
    return binary_search(array, target, start, mid - 1)
  elif array[mid] < target:
    return binary_search(array, target, mid + 1, end)


# N 입력받기
n = int(sys.stdin.readline().strip())

# 정수 공백구분 입력받고 리스트에 저장
array = list(map(int, sys.stdin.readline().split()))
array.sort() # 이진탐색 사용을 위해 정렬하기

# 찾을 요소 개수 M 입력받기
m = int(sys.stdin.readline().strip())

# 요소 M개 공백구분 입력받기
elements_to_find = list(map(int, sys.stdin.readline().split()))

# 이진탐색 실행 및 결과 출력
for element in elements_to_find:
  result = binary_search(array, element, 0, n - 1)
  if result == None: print(0)
  else: print(1)

  