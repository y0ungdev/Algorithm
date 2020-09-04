
def search_size :
    r_cnt = 0
    c_cnt = 0

    for i in range(r, N+2):
        if arr[i][c] == 0:
            break
        r_cnt += 1
    for j in range(c, N+2):
        if arr[r][j] == 0:
            c_cnt += 1

    ans.append(r_cnt, c_cnt)        # 리스트는 global 설정 없이 사용 가능

    init(r,c, r_cnt, c_cnt)         # 초기화

def init(r, c, r_cnt, c_cnt):
    for i in range(r, r+r_cnt):
        for j in range(c, c+c_cnt):
            arr[i][j] = 0           # 행렬의 요소를 모두 0으로 변경


    T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * (N+2)
    arr[0] = arr[N+1] = [0] * (N+2)

    for i in range(N):
        arr[i+1] = [0] + list(map(int, input().split())) + [0]

    ans = []

    for i in range(1, N+2):
        for j in range(1, N+2):
            if arr[i][j] != 0:
                search_size(i, j)

    ans = sorted(ans, key=lambda x : ((x[0]*x[1]), x[0]))

    print("#{} {}".format(tc, len(ans)), end=" ")
    for in range(len(ans)):
        print("{} {}" .format)