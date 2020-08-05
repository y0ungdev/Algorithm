#### 08 / 03 아파트 조망권

```python 
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



#### 08 /04 흙 Dump하기

```python 
for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        dump -= 1
    print(f'#{i} {max(boxes)-min(boxes)}')
```

<u>#최대와 최소 차이를 이용한다는 걸 알아챘으면 좋았을걸</u>



#### 08 / 05 100*100 2차 List의 최대값 구하기

```python
T = 10                                              # 테스트 넘버 입력
for t in range(1, T+1):                             # 배열 크기 설정
    number = int(input())                           # 배열로 입력받을 숫자
    lst = []                                        # 배열을 담을 리스트 만듦
    for i in range(100):                            # 100 * 100 크기의 배열 설정
        sub_lst = list(map(int,input().split()))    # 2차 리스트 설정
        lst.append(sub_lst)                         # 2차 리스트를 1차 리스트에 이서서 나오도록 출력

    res = []                                        # 결과(합)들을 담을 리스트 만듦

    for y in range(len(lst)):
        row_sum = 0
        for x in range(len(lst)):
            row_sum += lst [y][x]
        res.append(row_sum)                         # 결과 리스트에 행 내의 합을 넣음

    for x in range(len(lst)):
        col_sum = 0
        for y in range(len(lst)):
            col_sum += lst[y][x]
        res.append(col_sum)                         # 결과 리스트의 열 내의 합을 넣음

    cross1_sum = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == x:                              # 대각선의 합은 (1,1) (2,2) 이런 식으로 진행되니까 y==x
                cross1_sum += lst[y][x]
    res.append(cross1_sum)

    cross2_sum = 0
    for y in range(len(lst)):
        for x in range(len(lst)):
            if y == len(lst) - x:
                cross2_sum = lst[y][x]
    res.append(cross2_sum)

    print(f'#{t} {max(res)}')
```

<u>#2차원 배열</u>