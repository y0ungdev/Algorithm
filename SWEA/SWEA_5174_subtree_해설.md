### SWEA | 5174 | subtree



루트 노드 = 0 =?

공백 노드

왼쪽 서브트리 모두 탐색 후 루트 노드로 돌아옴 + 오른쪽 서브트리 모두 탐색 후 루트 노드로 돌아옴 = 모든 서브트리의 노드 개수를 알 수 있음

```python
for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)
    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        prnt, chld = arr[i], arr[i+1]
        if L[prnt] : R[prnt] = chld
        else: L[prnt] = chld
        P[chld] = prnt
    #전역변수 사용할 때
    # cnt = 0
    def traverse(v):
        if v == 0: return
        # cnt += 1
        l = traverse(L[v])
        r = traverse(R[v])
        return l + r + 1

    print(traverse(N))
    #전역변수 사용할 때 출력방식
    # print(cnt)
```



BFS로도 solving 가능