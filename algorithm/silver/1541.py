expression = input()  # 수식 입력 받기

# '-'를 기준으로 수식을 분할하여 리스트로 저장
split_expression = expression.split('-')

# 첫 번째 수식을 계산하여 초기값으로 설정
result = sum(map(int, split_expression[0].split('+')))

# 두 번째부터 마지막 수식까지 순회하며 값을 빼기
for i in range(1, len(split_expression)):
    result -= sum(map(int, split_expression[i].split('+')))

print(result)
