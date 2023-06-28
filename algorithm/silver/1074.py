def visit_position(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    area = half * half

    """
        1) area를 더해주는 이유는? : 
           - r, c가 1사분면에 존재한다면, r, c는 이미 지나온 4사분면의 숫자들을 건너뛰어야하기 때문
        2) c 자리에 c - half를 넣어주는 이유는?
            - 1사분면을 탐색할 것이기 때문에 c의 좌표값을 새로 update 해주는 것
    """
    if r < half and c < half: # 4사분면, Z의 첫번째
        return visit_position(n - 1, r, c)
    elif r < half and c >= half: # 1사분면, Z의 두번째
        return area + visit_position(n - 1, r, c - half)
    elif r >= half and c < half: # 3사분면, Z의 세번째
        # 마찬가지로, 3사분면이라면, 4사분면, 1사분면을 지나왔기 때문에 2개의 area를 건너뛰었음
        return 2 * area + visit_position(n - 1, r - half, c)
    else: # 4사분면, Z의 4번째
        return 3 * area + visit_position(n - 1, r - half, c - half)

n, r, c = map(int, input().split())
result = visit_position(n, r, c)
print(result)
