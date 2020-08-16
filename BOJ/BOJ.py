
nums_res = []
for i in range(10):
    num = int(input())
    nums_res.append(num%42)
nums_res = set(nums_res)
print(len(nums_res))
