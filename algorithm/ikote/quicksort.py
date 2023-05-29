# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
  
#   if start >= end: # if there's just one element
#     return
  
#   pivot = start # first element = pivot
  
#   left = start + 1 # second element
  
#   right = end
  
#   while (left <= right):
    
#     # moves right until it finds the element bigger than pivot
#     while (left <= end and array[pivot] >= array[left]):
#       left += 1

#     # moves left until it finds the element smaller than pivot
#     while (start < right and array[pivot] <= array[right]):
#       right -= 1

#     if (left > right): # 만약 left와 right 인덱스의 요소들이 엇갈렸다면, 작은 데이터와 피벗을 교체
#       array[right], array[pivot] = array[pivot], array[right]

#     else :
#         array[left], array[right] = array[right], array[left]

#   # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#   quick_sort(array, start, right - 1)
#   quick_sort(array, right + 1, end)


# quick_sort(array, 0, len(array) - 1)
# print(array)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  print(array)
  if len(array) <= 1:
    return array
  pivot = array[0] # 피벗은 첫 번째 원소
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽

  # 가장 중요! 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트를 반환.ㅅ
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))