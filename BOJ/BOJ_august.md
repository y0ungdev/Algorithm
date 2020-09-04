> 10818.

```python
N = int(input())

numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))
```

> 2562.

```python
nums_list = []
for i in range(9):
    nums_list.append(int(input()))

print(max(nums_list))
print(nums_list.index(max(nums_list))+1)
```

> 2577.

```python
A = int(input())
B = int(input())
C = int(input())

res = int(A)*int(B)*int(C)
res = str(res)

for i in range(0, 10):
    print(res.count(str(i)))
```

> 3052.

```python
nums_res = []
for i in range(10):
    num = int(input())
    nums_res.append(num%42)
nums_res = set(nums_res)	# 같은 수들을 교집합으로 묶음
print(len(nums_res))
```
