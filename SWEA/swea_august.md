### 08 / 01

> 2050 알파벳 숫자로 변환

```python
text = list(input())
for char in text :
    result = ord(char) - 64
    print(result, end = ' ')
```

**<u>#ord()</u>** : 문자의 ASCII 코드를 반환해 준다



> 2047 신문 헤드라인

```python 
string = str(input())
result = string.upper()
print(result)
```

**<u>#.upper()</u>**



> 2056 연월일 달력

```python 
T = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(T):
    date = input()
    mon = int(date[4:6])
    day = int(date[6:8])
    if 1<= mon <= 12 and 1<= day <= days[mon - 1]:
        result = date[0:4] + "/" + date[4:6] + "/" + date[6:8]
        print (f'#{t+1} {result}')
    else:
        print (f'#{t+1} -1')   
```

**<u>#slicing</u>**

리스트의 범위를 slicing한다. 리스트 L을 가정하고 L[a:c]라고 쓴다면 a번째 인덱스부터 c-1 인덱스까지 표시한다(c는 포함하지 않는다!).



### 08 / 02

> 2046 스탬프 찍기

```python
T = int(input())

for t in range(T):
    print("#",end = '')
```



> 2043 서랍의 비밀번호

```python
P, K = map(int,input().split())
pw_cnt = 1

for i in range(K): 
    if K == P :
        print(pw_cnt)
        break
    else:
        K += 1
        pw_cnt += 1
```



> 2029 몫과 나머지 출력하기

```python
T = int(input())
for t in range(T) :
    a, b = map(int, input().split())
    if a >= b :
        print(f'#{t+1} {a//b} {a%b} ')
    else:
        continue
```



> 1933 간단한 N의 약수

```python
N = int(input())
for n in range(1 , N+1):
    if N % n == 0 :
        print(n, end=' ')
```

**<u>#sorted</u>**

**<u>#.sort()</u>**

**<u>#for 문 안에서 정렬이 이미 되어서 돌아가므로 sort 등을 쓸 필요가 없음</u>**

> 1936 1대1 가위바위보

```python
A, B = map(int,input().split())

if A > B :
    print ("A")
elif A < B :
    print("B")
```



### 08 / 03

> 1206 조망권

````python 
for t in range (1, 11):
    n = int(input())
    apt = list(map(int, input().split()))
    cnt = 0

    for i in range(2, n-2):
        high = max(apt[i-2], apt[i-1], apt[i+1], apt[i+2])
        if apt[i] - high >0 :
            cnt += apt[i] - high
    print(f'#{t} {cnt}')

````

*문제에 그림자료가 추가되면 알고리즘 도출할 때 좀 감을 못 잡는 것 같다

```python 
# 교수님이 쓰신 해설
for t in range (1, 11):
    n = int(input())
    apt = list(map(int, input().split()))
    cnt = 0

    for i in range(2, n-2):
        high = max(apt[i-2], apt[i-1], apt[i+1], apt[i+2])
        if apt[i] - high >0 :
            cnt += apt[i] - high
    print(f'#{t} {cnt}')

```



### 08 / 07

> 4836 색칠하기

```python
T= int(input())
for t in range(1, T+1):
    main_lst = [[0 for i in range(10)] for j in range(10)]
    N = int(input())

    res = 0

    for i in range(N):
        r1, c1, r2, c2, col = map(int, input().split())
        for r in range(r1, r2 +1):
            for c in range(c1, c2+1):
                if col== 1:
                    if main_lst[r][c] == 0:                     # W
                        main_lst[r][c] = 1                      # W->R
                    elif main_lst[r][c] == 2:
                        main_lst[r][c] = 3
                        res += 1
                else :
                    if main_lst[r][c] == 0:
                        main_lst[r][c] = 2
                    elif main_lst[r][c] == 1:
                        main_lst[r][c] = 3
                        res += 1


    print(f'#{t} {res}')
```



> 4837 부분집합의 합

```python
# import sys
# sys.stdin = open("input.txt", "r")


set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

li = []
for i in range(1<< len(set)) :
    subset = []
    for j in range(len(set)):
        if i & (1 << j) :
            subset.append(set[j])
    li.append(subset)

T= int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    res = 0

    for z in li :
        if len(z) == n and sum(z) == k :
            res += 1

    print(f'#{t} {res}')

```



> 4839 이진탐색

```python

# import sys
# sys.stdin = open("input.txt", "r")

T= int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    start = 1
    end = P
    A_cnt = 0
    B_cnt = 0

    while start <= end :
        mid = int((start + end) // 2)
        A_cnt += 1
        if mid == Pa:
            break
        elif mid < Pa:
            start = mid
        else:
            end = mid
    start = 1
    end = P
    mid = int((start + end) // 2)

    while start <= end :
        mid = int((start + end) // 2)
        B_cnt += 1
        if mid == Pb:
            break
        elif mid < Pb:
            start = mid
        else:
            end = mid

    if A_cnt < B_cnt:
        print(f'#{t} A')

    elif A_cnt == B_cnt:
        print(f'#{t} 0')
    else:
        print(f'#{t} B')

```



> 4843 특별한 정렬

```python 
# import sys
# sys.stdin = open("input.txt", "r")

T= int(input())
for t in range(1, T+1):
    n = int(input())

    num_lst = list(map(int,input().split()))
    num_lst.sort()
    res_lst = []

    i=0
    j=len(num_lst)-1

    while i<j:
        res_lst.append(num_lst[j])
        res_lst.append(num_lst[i])
        i+=1
        j-=1

    result = ' '.join(map(str, res_lst[0:10]))

    print(f'#{t} {result}')

```



> 2007 패턴 마디의 길이

```python 
for t in range(int(input())):
    text = input()
    res = 0
    for i in range(1, 11):
        m = text[0:i]
        n = text[i:2*i]
        if m==n:
            res = i;
            break
    print(f'#{t+1} {res}')
```

