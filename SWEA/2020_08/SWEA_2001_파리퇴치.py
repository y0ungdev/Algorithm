

import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pad = [list(map(int, input().split())) for _ in range(N)]
    flies = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    fly += pad[r][c]
            flies.append(fly)

    print('# {} {}'.format(tc, max(flies)))
