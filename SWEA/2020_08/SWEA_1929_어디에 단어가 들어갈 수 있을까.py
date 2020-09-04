
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    # i, j 비교해서 둘 다 빈 칸이면 = 1
    # 둘 중 하나라도 0이면 =0
    # 가로부터 검사하기
    for i in range(N) :
        word_sum = 0
        for j in range(N):
            if arr[i][j] == 1 :
                # 글자 수 = sum
                word_sum += 1
                # sum == K가 되면 res += 1
                if word_sum == K :
                    res += 1
            else :
                word_sum = 0
            if word_sum > K:
                res -= 1
                word_sum = 0
     # 세로 검사하기
    for i in range(N):
        word_sum = 0
        for j in range(N):
            if arr[j][i] ==1:
                word_sum += 1
                if word_sum == K:
                    res += 1
            else:
                word_sum = 0

            if word_sum > K:
                res -= 1
                word_sum = 0
    print("#{} {}".format(tc, res))

