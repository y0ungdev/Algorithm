
import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    # print(puzzle)
    # 가로
    for x in range(N):
        sum = 0
        for y in range(N):
            if puzzle[x][y] == 1:
                sum += 1
                if sum == K:
                    res += 1
            else:
                sum = 0
            if sum > K :
                res -= 1
                sum = 0
    # 세로
    for x in range(N):
        sum = 0
        for y in range(N):
            if puzzle[y][x] == 1 :
                sum += 1
                if sum == K :
                    res += 1
            else :
                sum = 0
            if sum > K :
                res -= 1
                sum = 0
    print('#{} {}'.format(tc, res))
