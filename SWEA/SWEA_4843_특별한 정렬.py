
import sys
sys.stdin = open("4843.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    sortedNums = sorted(nums)

    res = []

    while len(res) < 10 :
        res.append(sortedNums[-1])
        res.append(sortedNums[0])
        sortedNums = sortedNums[1:len(sortedNums)-1]
    res = ' '.join(map(str, res))   # list 안의 요소들을 공백을 이용해 구분한다
    print('#{} {}'.format(tc, res))