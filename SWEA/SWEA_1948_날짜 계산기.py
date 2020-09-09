

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    res = 0
    for _ in range(m1, m2+1):
        if m1 == m2 :
            res = d2-d1+1
        else:
            res = d2+(days[m1-1]-d1+1)
            for i in range(m1+1, m2):
                res += days[i-1]

    print('#{} {}'.format(tc, res))
