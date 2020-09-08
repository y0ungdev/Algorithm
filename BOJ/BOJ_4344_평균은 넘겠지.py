

C = int(input())

for cs in range(1, C+1):
    N = list(map(int,input().split()))
    sum = 0
    for i in range(len(N)):
        sum += i
        i += 1
        avg = "%0.3f" % round (sum / len(N)*100)

    print('{}%'.format(avg))
