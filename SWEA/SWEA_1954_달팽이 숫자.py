



dx = [0,1,0,-1]
dy = [1,0,-1,0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 초기 좌표
    x = y = 0
    # 방향
    d = 0
    num = 1
    # 시작하는 부분은 항상 1이어야 하므로

    while num <= N*N :
        snail[x][y] = num
        num += 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d+1)%4
            x += dx[d]
            y += dy[d]

    print('#{}'.format(tc))

    for i in range(N):
        for j in range(N):
            print(snail[i][j], end = ' ')
        print()



