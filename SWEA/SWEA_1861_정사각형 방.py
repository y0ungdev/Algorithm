

import sys
sys.stdin = open("1861.txt", "r")


T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    rooms = []
    cnt_max = 0
    room = 0
    for _ in range(N):
        rooms.append(list(map(int, input().split())))
    for x in range(N):
        for y in range(N):
            cnt = 1
            que = [(x, y)]
            while que :
                quep = que.pop()
                for d in range(4):
                    if 0 <= quep[0] +dx[d] <N and 0<= quep[0] + dy[d] < N :
                        cnt += 1
                        que.append((quep[0]+dx[d], quep[0]+dy[d]))
            if cnt > cnt_max :
                cnt = cnt_max
                room = que[x][y]
            elif cnt == cnt_max :
                if room > que[x][y] :
                    room = que[x][y]



    print('#{} {} {}'.format(tc, room, cnt_max ))