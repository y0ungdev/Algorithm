

import sys
sys.stdin = open("input.txt", "r")



for t in range(int(input())):
    text = input()
    res = 0
    for i in range(1, 11):
        m = text[0:i]
        n = text[i:2*i]
        if m==n:
            res = i;
            break
    print(f'#{t} {res}')