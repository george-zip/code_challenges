"""
Leetcode 384: Shuffle an Array
- Given an integer array nums, design an algorithm to randomly shuffle the array. 
- All permutations of the array should be equally likely as a result of the shuffling.
- Implement the Solution class with reset and shuffle methods
- This implementation uses a Fisher-Yates shuffle because it's easy to 
follow and has time complexity of O(n).
"""

import random
from typing import List

class Solution:

	def __init__(self, nums: List[int]):
		self.nums = nums

	def reset(self) -> List[int]:
		"""
		Resets the array to its original configuration and return it.
		"""
		return self.nums

	def shuffle(self) -> List[int]:
		"""
		Returns a random shuffling of the array.
		"""
		cpy = self.nums[:]
		for i in range(len(self.nums) - 1):
			# Find the next struck number 
			j = random.randint(i, len(self.nums) - 1)
			# Move the the struck number to beginning of the list
			(cpy[i], cpy[j]) = (cpy[j], cpy[i])
		return cpy


obj = Solution([1, 2, 3, 4, 5, 6, 7, 8, 10])
param_2 = obj.shuffle()
print(param_2)
print(obj.reset())
