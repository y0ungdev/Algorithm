

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flies = [list(map(int,input().split())) for _ in range(N)]
    flapper = []
    tmp = []
    x = y = 0

    for _ in range(N):
        for i in range(M):
            for j in range(M):
                flapper.append(flies[x+i][y+j])
                flies_sum = sum(flapper)

    print('#{} {}'.format(tc, max(tmp)))
