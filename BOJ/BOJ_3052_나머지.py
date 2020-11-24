

nums_res = []
for i in range(10):
    num = int(input())
    nums_res.append(num%42)
nums_res = set(nums_res)	# 같은 수들을 교집합으로 묶음
print(len(nums_res))