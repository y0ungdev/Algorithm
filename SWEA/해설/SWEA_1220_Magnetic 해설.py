

for tc in range(1, 11) :
    N = int(input())
    arr = [input().split() for _ in range(N)]

    cnt = 0

    for i in range(N):
        # 현재 만나야 하는 색깔을 1로 두고 진행
        state = 1
        for j in range(N):

            if state == 1 and arr[j][i] == '1':
                state = 2
            elif state == 2 and arr[j][i] == '2':
                state = 1
                cnt += 1

    print('#{} {}'.format(tc, cnt))