def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  elif array[mid] < target:
    return binary_search(array, target, mid + 1, end)

# 원소의 갯수, 찾고자하는 요소
n, target = list(map(int, input().split()))

# 원소의 갯수만큼 공백 구분 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print('{}은 {}번째 인덱스에 있습니다.'.format(target, result))

    