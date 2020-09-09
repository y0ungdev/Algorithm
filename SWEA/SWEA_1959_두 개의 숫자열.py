

import sys
sys.stdin = open("1959.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_num = list(map(int, input().split()))
    M_num = list(map(int, input().split()))
    res = []
    if N < M :
        for i in range(M-N+1):
            calc = []
            for j in range(N):
                calc.append(N_num[j]*M_num[i+j])
            res.append(sum(calc))
    else:
        for i in range(N-M+1):
            calc = []
            for j in range(M):
                calc.append(M_num[j]*N_num[i+j])
            res.append(sum(calc))

    print('#{} {}'.format(tc, max(res)))
