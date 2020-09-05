

N = int(input())

minN = 0
maxN = 0
for i in range(1, N+1):
    nums = list(map(int, input().split()))
    for i in nums :
        if i < i+1 :
            minN = nums[i]
        else :
            minN = nums[i+1]
            i += 1
        print(minN)


# 크기순으로 정렬한 후에 맨 앞의[0] 것과 맨 뒤의 [-1] 것을 인덱스로 출력하기
# 내장함수 min(), max() 쓰기


