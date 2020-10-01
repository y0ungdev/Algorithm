

C = int(input())

for tc in range(C):
    scores = list(map(int, input().split()))
    avg = (sum(scores) - scores[0]) / (len(scores) - 1)
    stdt_cnt = 0
    for score in scores[1:]:
        if score > avg:
            stdt_cnt += 1
    rat = (stdt_cnt / (len(scores) - 1))*100
    print('{0:.3f}%'.format(rat))




