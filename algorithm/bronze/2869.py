import math

# 달팽이가 낮에 올라갈 수 있는 높이 A, 밤에 내려오는 높이 B, 나무 막대의 높이 V 입력
A, B, V = map(int, input().split())

# 필요한 날짜 수 계산
days = math.ceil((V - B) / (A - B))

print(days)
