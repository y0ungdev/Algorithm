
def check() :
    for i in range(9):       # 9*9 크기의 행렬

        row = [0]*10
        col = [0]*10

        for j in range(9):
            num1 = sudoku[i][j] # 행 검사
            num2 = sudoku[j][i] # 열 검사
            if row[num1]:       # num1 값에 False 값이 온다면 0을 반환
                return 0
            if col[num2]:
                return 0

            row[num1] = col[num2] = 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0]*10 # 3*3 검사 실행
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1


T = int(input())

for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if check():
        print("#{} 1". format(tc))
    else :
        print("#{} 0". format(tc))