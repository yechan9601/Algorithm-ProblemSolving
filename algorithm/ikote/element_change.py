N, K = map(int, input().split())

A = [x for x in list(map(int, input().split()))]
B = [x for x in list(map(int, input().split()))]

# Use standard library: list.sort()
# A.sort()
# B.sort(reverse=True)

# Selection sort: 처리되지 않은 데이터를 제외하고 가장 작은/큰 데이터를 처리되지 않은 첫번째 요소와 스왑
# for i in range(len(A)):
#   min_index = i
#   for j in range(i + 1, len(A)):
#     if A[min_index] > A[j]:
#       min_index = j
#   A[min_index], A[i] = A[i], A[min_index]

# for i in range(len(B)):
#   max_index = i
#   for j in range(i + 1, len(B)):
#     if B[max_index] < B[j]:
#       max_index = j
#   B[max_index], B[i] = B[i], B[max_index]


# Insertion sort: 첫번째 데이터를 제외하고, 다음 데이터를 선택하여 순차적(N-1, N-2...)으로 삽입할 위치를 결정
# for i in range(1, len(A)):
#   for j in range(i, 0, -1):
#     if A[j] < A[j - 1]:
#       A[j], A[j - 1] = A[j - 1], A[j]
#     else:
#       break;

# for i in range(1, len(B)):
#   for j in range(i, 0, -1):
#     if B[j] > B[j - 1]:
#       B[j], B[j - 1] = B[j - 1], B[j]
#     else:
#       break;


# Quick sort:
def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

A = quick_sort(A)
B = quick_sort(B)
B.reverse()


for i in range(K):
  A[i], B[i] = B[i], A[i]

print(sum(A))
  