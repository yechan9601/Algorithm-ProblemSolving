# O(n^2), 최선의 경우 O(n)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break;

print(array) # 실행결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]