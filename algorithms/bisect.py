import bisect
def search(nums, target):
    index = bisect.bisect_left(nums, target)
     
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
 
nums_len = int(input())
nums = list(map(int, input().split()))
target_len = int(input())
targetList = list(map(int, input().split()))
result = []
for target in targetList:
  result.append(search(nums, target))
print(*result, sep = " ")