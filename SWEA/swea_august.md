### 08 / 01

> 2050 알파벳 숫자로 변환

```python
text = list(input())
for char in text :
    result = ord(char) - 64
    print(result, end = ' ')
```

<u>#ord()</u>



> 2047 신문 헤드라인

```python 
string = str(input())
result = string.upper()
print(result)
```

<u>#.upper()</u>



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

<u>#slicing</u>