# <좌표 정렬하기>

# n 입력받기
n = int(input())

# 둘째줄부터 N개의 줄에는 i번점의 위치 x[i], y[i]가 주어진다.
array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

# 정렬 수행: selection sort, insertion sort, quick sort, merge sort, counting sort, standard lib
array.sort(key = lambda x : (x[0], x[1]))


# 결과 출력
for i in range(len(array)):
  print(array[i][0], array[i][1])