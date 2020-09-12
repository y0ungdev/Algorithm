
import sys
sys.stdin = open("1966.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    tt = input()
    t = list(map(int, input().split()))
    t.sort()
    result = ''
    for i in t:
        result += str(i) + ' '

    print(f'#{test_case} {result}')