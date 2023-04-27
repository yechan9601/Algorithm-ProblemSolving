def count_vowels(sentence):
  # 소문자로 변환
  sentence = sentence.lower()
  # 모음 리스트
  vowels = ['a', 'e', 'i', 'o', 'u']
  # 모음 개수 초기화
  count = 0
  # 문장을 순회하면서 모음 개수 세기
  for char in sentence:
    if char in vowels:
      count += 1
  return count


sentences = []
while True:
  sentence = input()
  if sentence == '#':
    break
  sentences.append(sentence)

for sentence in sentences:
  print(count_vowels(sentence))
