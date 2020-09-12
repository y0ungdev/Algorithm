

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    while N != 0 :
        if N >= 50000 :
            d1 = N // 50000
        else :
            d1 = 0
        N = N % 50000
        if N >= 10000 :
            d2 = N // 10000
        else:
            d2 = 0
        N = N % 10000
        if N >= 5000:
            d3 = N // 5000
        else:
            d3 = 0
        N = N % 5000
        if N >= 1000:
            d4 = N // 1000
        else:
            d4 = 0
        N = N % 1000
        if N >= 500:
            d5 = N // 500
        else:
            d5 = 0
        N = N % 500
        if N >= 100:
            d6 = N // 100
        else:
            d6 = 0
        N = N % 100
        if N >= 50:
            d7 = N // 50
        else:
            d7 = 0
        N = N % 50
        if N >= 1:
            d8 = N // 10
        else:
            d8 = 0
        N = N // 10
        break


    print('#{} \n{} {} {} {} {} {} {} {}'.format(tc, d1, d2, d3, d4, d5, d6, d7, d8))