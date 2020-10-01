
#오잉 런타임 에러 뭐야

N = int(input())
sums = 0
for i in range(N):
    nums = list(map(int,input()))
    for num in nums:
        sums += num
    print(sums)