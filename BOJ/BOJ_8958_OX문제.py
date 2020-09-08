

T = int(input())

for tc in range(1, T+1):
    scores = input()
    res = 0
    cnt = 0
    for i in range(len(scores)) :
        if scores[i] == "O":
            cnt += 1
            res += cnt
        elif scores[i] == "X":
            res += 0
            cnt = 0
    print(res)