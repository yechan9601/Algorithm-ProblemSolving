"""
정당성 분석:
  종료 시간이 이를 수록 최대 회의를 arrange 할 수 있다.
  실수했던 부분: interval이 짧을 수록 최대 회의를 arrange 할 수 있다고 생각함. 정렬을 interval이 짧은 순으로 진행했었음.
"""

# 입력 받기
n = int(input())  # 회의의 수
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의 선택하기
count = 0
end_time = 0
for meeting in meetings:
    if meeting[0] >= end_time:
        count += 1
        end_time = meeting[1]

# 결과 출력
print(count)
