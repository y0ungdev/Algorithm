### 07 / 30

> 2025 N줄 덧셈

```python 
n = int(input())
n_sum = 0
for i in range(1, n+1):    
    n_sum += i
print(n_sum)
```



> 1938 아주 간단한 계산기

```python 
a, b = map(int, input().split())

print(a + b )

if a > b :
    print(a - b)
else:
    print(abs(b - a))

print(a * b)

if a > b :
    print(a // b)
else :
    print (b // a)
```



> 2070 큰 놈, 작은 놈, 같은 <u>놈</u>

```python
T = int(input())
 
for t in range(1, T+1):
    a, b = map(int, input().split())
    if a > b :
        result ='>'
    elif a == b :
        result ='='
    else :
        result ='<'
    print(f'#{t} {result}')
```

<u>#f string interpolation</u>

**<u>#.split()</u>**



> 2071 평균값 구하기

```python 
n = int(input())
 
for i in range(n) :
    numbers = list(map(int, input().split()))
    avg = round(sum(numbers)/ len(numbers))
 
    print(f'#{i+1} {avg}')
```

**<u>#map()</u>** : 인자 2개 필요함 ~~1개 넣어서 에러 났었음.~~

ex) map(f, iterable) : 함수 f를 iterable한 자료형을 통해 수행한 결과를 묶어서 돌려준다



>  2072 홀수만 더하기

```python
n = int(input())

for i in range(n) :
    numbers = list(map(int, input().split()))
    odd_sum = 0
    for j in range(len(numbers)):
        if numbers[j] % 2 == 1:
            odd_sum = odd_sum + numbers[j]
        else:
            continue
    print(f'#{i+1} {odd_sum}')

```



### 07 / 31

> 2058 자릿수 더하기

```python
n = int(input())
def n_digit_sum(n) :
    number = str(n)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum

print(n_digit_sum(n))
```



> 2068 최댓값 구하기

```python 
n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    n_max = numbers[0] 
    for j in range(len(numbers)):
        if n_max <= numbers[j]:
            n_max = numbers[j]
        else:
            continue
    
    print(f'# {i+1} {n_max}')
```



> 2063 중간값 찾기

```python
n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[int(n//2)])
```

**#.sort()**