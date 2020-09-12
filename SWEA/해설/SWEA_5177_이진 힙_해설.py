

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item




for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0] * (N+1)
    hsize = 0

    c = hsize;
    p = hsize // 2
    while:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
        else:
            return