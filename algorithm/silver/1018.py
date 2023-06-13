def check_chessboard(board):
    start_w, start_b = 0, 0

    # 체스판 시작이 W로 시작하는 경우와 B로 시작하는 경우를 나눠서 확인
    # W로 시작하는 경우와 B로 시작하는 경우의 최소 칠해야 하는 개수를 비교하여 작은 값 반환
    for i in range(8):
        for j in range(8):
            # W로 시작하는 체스판과 비교
            if (i + j) % 2 == 0:
                if board[i][j] != 'W':
                    start_w += 1
            else:
                if board[i][j] != 'B':
                    start_w += 1

            # B로 시작하는 체스판과 비교
            if (i + j) % 2 == 0:
                if board[i][j] != 'B':
                    start_b += 1
            else:
                if board[i][j] != 'W':
                    start_b += 1

    return min(start_w, start_b)


n, m = map(int, input().split())
chessboard = []

for _ in range(n):
    row = input()
    chessboard.append(row)

min_paint = float('inf')

# (0, 0)부터 체스판을 8x8 크기로 잘라서 확인
for i in range(n - 7):
    for j in range(m - 7):
        # 8x8 크기의 체스판으로 자르기
        sub_board = [row[j:j+8] for row in chessboard[i:i+8]]
        paint_cnt = check_chessboard(sub_board)
        min_paint = min(min_paint, paint_cnt)

print(min_paint)
