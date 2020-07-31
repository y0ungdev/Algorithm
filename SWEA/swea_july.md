### 07 / 30

> 2070 큰 놈, 작은 놈, 같은 놈

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



> 2071 평균값 구하기

```python 
n = int(input())
 
for i in range(n) :
    numbers = list(map(int, input().split()))
    avg = round(sum(numbers)/ len(numbers))
 
    print(f'#{i+1} {avg}')
```



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

