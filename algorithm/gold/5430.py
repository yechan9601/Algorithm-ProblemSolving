from collections import deque

T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    p = input()  # 수행할 함수
    n = int(input())  # 배열의 길이
    arr = input()[1:-1].split(",")  # 배열의 요소들을 입력 받음
    if n == 0:
        arr = deque()
    else:
        arr = deque(arr)
    
    is_reversed = False  # 배열이 뒤집혔는지 여부
    error = False  # 에러 발생 여부
    
    for command in p:
        if command == "R":
            is_reversed = not is_reversed
        elif command == "D":
            if len(arr) == 0:
                error = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()
    
    if error:
        print("error")
    else:
        if is_reversed:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
