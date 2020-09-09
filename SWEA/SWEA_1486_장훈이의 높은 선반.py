

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
# 점원들 키 리스트에서 부분집합 생성
    pwrset = []
    for i in range(1 << N):
        h_sum = 0
        for j in range(len(H)):
            if i &(1 << j):
                h_sum += H[j]

            if h_sum >= B:
                pwrset.append(h_sum - B)

    print('#{} {}'.format(tc, min(pwrset) ))