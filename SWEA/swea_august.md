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

