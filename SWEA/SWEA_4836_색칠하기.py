

import sys
sys.stdin = open('4836.txt', "r")

T = int(input())
for tc in range(1, T+1):
    board = [[0]*10 for _ in range(10)]
    sum = 0
    N = int(input())
    for i in range(N):
        x1, y1, x2, y2, col = map(int, input().split())

        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                board[r][c] += col

    for r in range(10):
        for c in range(10):
            if board[r][c] == 3:
                sum += 1

    print('#{} {}'.format(tc, sum))

