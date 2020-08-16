


import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for x in range(9):
        hor = set()
        ver = set()
        for y in range(9):
            hor.add(arr[x][y])
            ver.add(arr[y][x])
        if len(hor) != 9:
            result = 0
            break
        if len(ver) != 9:
            result = 0
            break

    trg = 0
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            rec = set()
            for i in range(3):
                for j in range(3):
                    rec.add(arr[x + i][y + j])
            if len(rec) != 9:
                result = 0
                trg = 1
                break
        if trg :
            break
    print(f'#{t} {result}')