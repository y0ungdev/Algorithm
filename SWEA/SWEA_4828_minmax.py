
#SWEA_4828_Min Max

import sys
sys.stdin = open("input.txt", "r")


def num_max(num_list):
    num_max = num_list[0]
    for m in range(1, num_list+1):
        if num_list[m] > num_max:
            num_max = num_list[m]
            return num_max

def num_min(num_list):
    num_min = num_list[0]
    for n in range(1, num_list+1):
        if num_list[n] < num_min :
            num_min = num_list[n]
            return num_min



for tc in range(1, (int(input()))+1):
    num_cnt = int(input())
    num_list = list(map(int, input().split()))

    res = max(num_list) - min(num_list)

    print('#{} {}'.format(tc, res))

