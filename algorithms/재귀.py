def search(nums, target):
  def binary_search(left, right):
    if left <= right:
      mid = (left+right) // 2
      if nums[mid] < target:
        return binary_search(mid + 1, right)
      elif nums[mid] > target:
        return binary_search(left, mid-1)
      else:
        return mid
    else:
       return -1
  return binary_search(0, len(nums)-1)
 
nums_len = int(input())
nums = list(map(int, input().split()))
target_len = int(input())
targetList = list(map(int, input().split()))
result = []
for target in targetList:
  result.append(search(nums, target))
print(*result, sep = " ")