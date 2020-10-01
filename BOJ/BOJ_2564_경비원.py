

x, y = list(map(int, input().split()))
block = [list(0 for _ in range(x)) for _ in range(y)]
stores = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for _ in range(1, stores):
    # 상점 위치 좌표 입력 받아 오기
    locx, locy = list(map(int, input().split()))
    # 시작 좌표 입력 받아 오기
    stx, sty = list(map(int, input().split()))
    # 모든 경로 리스트에 넣은 후 최단 거리(최소값) 출력
    route = []
    for d in range(4):
        nx = stx + dx[d]
        ny = sty + dy[d]
        if nx > x or ny > y :
            break
        else:
            # nx랑 ny가 목표 지점까지 가면서 좌표가 변할 때마다 0에서 1로 해당 값을 바꾸고 리스트에 추가
            # nx랑 ny가 상점의 위치 좌표와 동일해지면 해당 좌표를 리스트에 추가한 후 리스트의 길이를 출력(=경로 길이)
            if nx == locx and ny == locy:
                route.append((nx,ny))
                print(len(route))
                pass
            #그렇지 않은 경우에는 계속 진행함
            else:
                continue










