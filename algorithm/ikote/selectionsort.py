# O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i
	for j in range(i + 1, len(array)): # 처리된 데이터를 제외
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array) # 실행결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
