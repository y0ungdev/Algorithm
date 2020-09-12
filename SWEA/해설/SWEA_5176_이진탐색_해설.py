
for tc in range(1, int(input())+1):
    N = int(input())
    Tr = [0] * (N+1)

    cnt = 1
    def inorder(v):
        global cnt
        if v > N : return
        inorder(v * 2)
        T[v] = cnt
        cnt += 1
        inorder(v * 2 + 1)

    inordr(1)
    print(Tr[1], Tr[N//2])