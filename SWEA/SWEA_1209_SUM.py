

import sys
sys.stdin = open("input.txt", "r")



for tc in range(1, int(input())+1) :
    # 데이터 입력을 2차원 배열로 받아와야 함.
    # 빈 리스트 만들어서 여기 안에 숫자 넣기
    square_lst = []

    for i in range(100):
        # 숫자 데이터 리스트로 넣어서
        temp_lst = list(map(int, input().split()))
        # 2차원 배열로??
        square_lst.append(temp_lst)

    max_sum = 0
    sum_lst = []
# 가로, 세로 합 구하기
    for i in range(100):
        sum_h = 0
        sum_v = 0
        for j in range(100):
            sum_h += square_lst[i][j]
            sum_v += square_lst[j][i]
        sum_lst.append(sum_h)
        sum_lst.append(sum_v)

        # 대각선(좌상-우하) 합 구하기
    for i in range(100):
        sum_d1 = 0
        for j in range(100):
            if i == j:
                sum_d1 += square_lst[i][j]
        sum_lst.append(sum_d1)
        # 대각선(우상-좌하) 합 구하기
    for i in range(len(square_lst)):
        sum_d2 = 0
            for j in range(len(square_lst)):
                if i == len(square_lst) - j :
                    sum_d2 += square_lst[i][j]
        sum_lst.append(sum_d2)

    print('#{} {}'.format(tc, max(sum_lst)))
