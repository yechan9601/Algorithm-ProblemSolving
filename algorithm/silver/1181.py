# def SelectionSort(arrayOfStr):
#   for i in range(len(arrayOfStr)):
#     min_idx = i
#     # 처리되지 않은 데이터 중에서 가장 길이가 짧은 요소의 인덱스 찾기
#     for j in range(i + 1, len(arrayOfStr)):
#       if len(arrayOfStr[min_idx]) > len(arrayOfStr[j]):
#         min_idx = j
#     # swap
#     arrayOfStr[i], arrayOfStr[min_idx] = arrayOfStr[min_idx], arrayOfStr[i]
#   return arrayOfStr

import sys

n = int(sys.stdin.readline().strip())
words = []

# 우선 단어들을 순서대로 리스트에 넣기
for _ in range(n):
  word = sys.stdin.readline().strip()
  # 단, 중복된 단어는 하나만 남기고 제거해야 한다.
  if word not in words:
    words.append(word)

words.sort() # 사전순
words.sort(key = len) # 문자열 길이순

# # 결과 출력
for word in words:
  print(word)
      
