"""
Leet code 26: Remove Duplicates from Sorted Array
"""

class Solution:
  def removeDuplicates2(self, nums) -> int:
    """Iterate through nums and delete duplicates"""
    idx = 0
    num_len = len(nums)
    while idx < num_len:
      if idx:
        if nums[idx] == nums[idx - 1]:
          del nums[idx]
          num_len -= 1
          continue
      idx += 1
    return idx
        
  def removeDuplicates(self, nums) -> int:
    """Iterate through nums and swap unique and duplicates"""
    unique_idx = 0
    for cur_idx in range(len(nums)):
      if nums[cur_idx] != nums[unique_idx]:
        unique_idx += 1
        nums[unique_idx] = nums[cur_idx]
    return unique_idx + 1
            

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
len = s.removeDuplicates(nums)
print(len)
print(nums[:len])
