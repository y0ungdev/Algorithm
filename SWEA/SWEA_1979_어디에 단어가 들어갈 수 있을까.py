
import sys
sys.stain = open("1979.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)
    # 델타 이동 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 시작점 설정
    xS = yS = 0
    blank = []
    for i in range(4):
        xNew = xS + dx[i]
        yNew = yS + dy[i]
        if 0 <= xNew < N and 0 <= yNew <N :
            if puzzle[xNew][yNew] != 0 :
                blank.append((xNew, yNew))
            else :
                break

    print('#{} {}'.format(tc, len(blank)))