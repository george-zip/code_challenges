"""
Leetcode problem 88: Merge Sorted Array
Store results in nums1
"""

from typing import List
import copy


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Runtime complexity is O(m + n) but there's a trade-off in that we copy nums1 
		"""
		nums1_cpy = copy.deepcopy(nums1)
		i, j = 0, 0
		while i + j < n + m:
			if i >= m:
				nums1[i + j] = nums2[j]
				j += 1
			elif j >= n:
				nums1[i + j] = nums1_cpy[i]
				i += 1
			elif nums1_cpy[i] < nums2[j]:
				nums1[i + j] = nums1_cpy[i]
				i += 1
			else:
				nums1[i + j] = nums2[j]
				j += 1


sol = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
assert nums1 == [1]

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sol.merge(nums1, m, nums2, n)
assert nums1 == [1, 2, 2, 3, 5, 6]
