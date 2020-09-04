

import sys
sys.stdin = open("input.txt", "r")


def going():

#
# 도착 지점에서 역순으로 진행 => 상,좌/우 2가지 경우 고려
# 지나온 길 기억(재방문 X) => 리스트 등에 저장해두기
# 갈림길 = 위로 가든가 or 좌/우 중 하나로 가든가
# 위로 가려면 => Y좌표가 +1 되는 지점으로 이동
# 좌/우 중 하나로 가려면 => Y좌표는 동일하되 X좌표 -1 or +1
# Y = 0 도착했을 때의 arr[i][j] 출력 => X좌표 get


T = int(input())a

for tc in range(1, T+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]:
    print(ladder)

    Y_start = 99
    X_start = ladder[99].["2"]


