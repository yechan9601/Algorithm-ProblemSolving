# 입력 받기
n = int(input())

# 최소 봉지 개수 구하기
count = 0

# 5로 최대한 많이 나누기
while n >= 0:
    if n % 5 == 0:  # 5로 나누어 떨어지면
        count += n // 5  # 5로 나눈 몫을 봉지 개수에 더함
        print(count)
        break
    n -= 3  # 5로 나누어 떨어지지 않으면 3씩 빼기
    count += 1

# 3과 5로 나누어 떨어지지 않는 경우
if n < 0:
    print(-1)
