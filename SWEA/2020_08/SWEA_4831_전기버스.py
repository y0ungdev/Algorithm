
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    K, N, M = list(map(int,input().split()))
    # 정류소 목록을 리스트로 받았어야 했음.
    char = 0
    for i in range(1, N+1):
        if N[i] + K != M[i] :
            i = max(N[0:i])
            char += 1
        else:
            i += 1

    print('#{} {}'.format(tc, char))


