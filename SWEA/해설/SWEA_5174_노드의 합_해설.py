

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    Tr = [0] * (N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        Tr[num] = val

    for i in range(N-M, 0, -1):
        T[i] = T[i*2]+T[i*2+1]
        if i * 2 + 1 <= N:
            T[i] += T[i*2+1]
    # def DFS(v):
    #     if v > N : return 0
    #     l = DFS(v*2)
    #     r = DFS(v*2+1)
    #     Tr[v] += l + r
    #     return Tr[v]

    # DFS(1)

    # print(T[L])