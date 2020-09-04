
import sys
sys.stdin = open("input.txt", "r")


# 우상 우 우하 하 좌하 좌 좌상 상
# delta = [(1,-1), (1,0), (1,1), (0,1), (-1, 1), (-1,0), (-1,-1)]
delta_y = [-1, 1, 1, 0, -1, -1, -1, 0]
delta_x = [1, 0, 1, 1, 1, 0, -1, -1]


# 보드판 리셋 함수
def setting(N):
    # 초기 돌 위치 설정
    init = N // 2
    board[init][init] = 2
    board[init+1][init] = 1
    board[init][init+1] = 1
    board[init+1][init+1] = 2

    other_colour = -1
    if color == 1:
        other_colour == 2:
    else:
        other_colour == 1


# 돌 진행 범위 설정 - 0보다 작거나 N보다 크면 안됨
def range_check(x,y,colour):
    if x<0 or x>=N or y<0 or y>= N:
        return 0
    if not board[x][y]:
        return 0
    if board[x][y] == colour:
        return 2
    return 1

# 돌 뒤집기
def flip_check(x,y,colour):
    # 8방향 검사해야 하므로 범위는 8까지
    for i in range(8):
        move_x = delta_x[i]
        move_y = delta_y[i]
        # 뒤집은 돌 넣을 리스트 만듦

        while True:
            # 돌 이동하기 - 이동 거리 보고 범위 내에 있는지 없는지 체크
            moving = range_check(x + move_x, y + move_y, colour)
            # 이동 거리가 범위 밖이면 함수 종료
            if not moving:
                break
            if moving ==
                # ABA -> AAA가 되게끔 돌 색을 바꾸는 코드를 작성해야 하는데
                # 이걸 어떻게 작성해야 하는지 모르겠어요ㅠㅠ
                break

       # 해당 돌 색깔 출력
        board[x][y] = colour
# 현재 상태 돌 개수 세기
def cnt_colour(N):
    for colours in board:
        # 1이면 흰색 돌 세고 2이면 흑색 돌 세기
        cnt_w += colours.count(1)
        cnt_b += colours.count(2)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 보드판을 N*N의 0으로 초기화
    board = [[0] * N for _ in range(N)]
    # 초기 설정 함수 호출
    setting(N)
    # M번 돌을 둘 수 있으므로 M번 반복
    for _ in range(M):
        # 위치, 색깔 입력 받아오기
        x, y, colour = map(int,input().split())
        # N=4로 했지만 실제 인덱스는 0~3이니까 맞춰 주어야 함
        flip_check(x-1, y-1, colour)
        # 세는 거 초기화시키고
        cnt_w = 0
        cnt_b = 0
        # 세는 함수 호출 - 인자는 N
        cnt_colour(N)

    print('# {} {} {}'.format(tc, cnt_w, cnt_b))










