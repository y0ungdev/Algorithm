
import sys
sys.stdin = open("1974.txt", "r")



T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 가로 확인
    for x in range(9):
        xV = set()
        for y in range(9):
            xV.add(sudoku[x][y])
        if len(xV) != 9 :
            result = 0
            break
    # 세로 확인
    for x in range(9):
        yV = set()
        for y in range(9):
            yV.add(sudoku[y][x])
        if len(yV) != 9:
            result = 0
            break
    # 3*3 정사각형 확인
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sqV = set()
            for unit in range(3):
                sqV.update(sudoku[x+unit][y:y+3])
            if len(sqV) != 9:
                result= 0
                break

    print('#{} {}'.format(tc, result))