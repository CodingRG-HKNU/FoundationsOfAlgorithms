def binary_search(nums, target):
  left, right = 0, len(nums)-1
  while left <= right:
    mid = (left+right) // 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    else: 
      return mid
  return -1
 
nums_len = int(input())
nums = list(map(int, input().split()))
target_len = int(input())
targetList = list(map(int, input().split()))
result = []
for target in targetList:
  result.append(binary_search(nums, target))
print(*result, sep = " ")