
def check():
    for i in range(N):
        # 가로 검사
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            if tmp == tmp[::-1]:
                return tmp
        # 세로 검사
        for j in range(N-M+1):
        # 세로 슬라이싱은 불가능하므로 빈 리스트에 쌓아 넣기
            tmp = []
            for k in range(N):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    words = [list(input()) for _ in range(N)]

    ans = check()

    print("#{} {}".format(tc, ''.join(ans)))
    