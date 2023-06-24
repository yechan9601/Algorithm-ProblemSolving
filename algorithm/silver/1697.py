from collections import deque

# 입력 받기
n, k = map(int, input().split())  # 현재 위치(n)와 목표 위치(k)

# 최단 시간 기록 리스트 생성
time = [-1] * 100001  # 최대 범위로 초기화
time[n] = 0  # 시작 위치의 시간은 0

# BFS 실행
def bfs():
    queue = deque([n])  # 큐에 시작 위치 추가
    
    while queue:
        x = queue.popleft()
        
        # 현재 위치에서 가능한 모든 이동 방법 확인
        for nx in [x-1, x+1, x*2]:
            # 이동한 위치가 범위 내에 있고, 아직 방문하지 않은 위치인 경우
            if 0 <= nx <= 100000 and time[nx] == -1:
                time[nx] = time[x] + 1  # 시간 기록
                queue.append(nx)  # 큐에 추가

        # 목표 위치에 도달한 경우 종료
        if x == k:
            return time[k]

# BFS 실행 및 결과 출력
result = bfs()
print(result)
