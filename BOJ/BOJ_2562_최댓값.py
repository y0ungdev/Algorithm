
# for _ in range(9):
# #     nums = int(input())
# #
# #     print(max(nums))
# #     print(max(nums[i]))
nums_list = []
for i in range(9):
    nums_list.append(int(input()))

print(max(nums_list))
print(nums_list.index(max(nums_list))+1)