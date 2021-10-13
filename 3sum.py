"""
Leet code 15: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
There are a few versions here that the different approaches I tried.
From top to bottom:
1. 'n_sum_brute_force`: A recursive function that tests every combination of numbers to see if the sum equals 0.
2. `n_sum_iterative`: An iterative version that tests all possible combinations.
3. `n_sum_sorted`: An iterative function that sorts the input and uses binary search to find the right value.
4. `n_sum_dictionary`: This function creates a map from the array values to indices so that the right values can be found very
quickly. This ended up being the fastest version by far.
"""

from typing import List
import random
import time


def n_sum_brute_force(nums: List[int], n: int, target: int, so_far: List[int]) -> tuple:
	"""
	Recursively compare every combination of values against target
	"""
	if len(so_far) == n:
		values = [nums[i] for i in so_far]
		if sum(values) == target:
			return tuple(sorted(values))
	else:
		i = so_far[-1] + 1 if so_far else 0
		unique_results = set()
		while i < len(nums):
			result = n_sum_brute_force(nums, n, target, so_far + [i])
			if result:
				if len(so_far) == n - 1:
					unique_results.add(result)
				else:
					unique_results.update(result)
			i += 1
		return tuple(unique_results)
	return None


def n_sum_iterative(nums: List[int], target: int) -> List:
	"""
	Iteratively compare every combination of values against target
	"""
	results = set()
	i = 0
	while i < len(nums):
		j = i + 1
		while j < len(nums):
			k = j + 1
			while k < len(nums):
				if nums[i] + nums[j] + nums[k] == target:
					results.add(tuple(sorted([nums[i], nums[j], nums[k]])))
				k += 1
			j += 1
		i += 1
	return tuple(results)


def bin_search(nums: List[int], start_idx: int, end_idx: int, target: int) -> int:
	idx = (end_idx + start_idx) // 2
	while end_idx >= start_idx:
		if nums[idx] == target:
			return idx
		if nums[idx] > target:
			end_idx = idx - 1
		else:
			start_idx = idx + 1
		idx = (end_idx + start_idx) // 2
	return None


def n_sum_sorted(nums: List[int]) -> List:
	"""
	Sorts input and uses binary search to find missing value
	"""
	results = set()
	sorted_nums = sorted(nums)
	for i in range(len(sorted_nums) - 2):
		for j in range(len(sorted_nums) - 1, i, -1):
			k = bin_search(sorted_nums, i + 1, j - 1, -(sorted_nums[i] + sorted_nums[j]))
			if k:
				results.add(tuple([
					sorted_nums[i],
					sorted_nums[k],
					sorted_nums[j]
				]))
	return list(results)


def n_sum_dictionary(nums: List[int]) -> List:
	"""
	Uses a map of values to indices to locate the right value. No need to sort the input.
	"""
	results = set()
	value_hash = {nums[i]: i for i in range(len(nums))}
	for i in range(len(nums) - 2):
		for j in range(len(nums) - 1, i, -1):
			k = value_hash.get(-(nums[i] + nums[j]))
			if k is not None and i != k and j != k:
				results.add(tuple(sorted([
					nums[i],
					nums[k],
					nums[j]
				])))
	return list(results)


class Solution:

	def threeSum(self, nums: List[int]) -> List[List[int]]:
		return n_sum_dictionary(nums)


n = 5000
nums = [random.randint(-n, n) for _ in range(n)]

sol = Solution()
start_time = time.time()
result = sol.threeSum(nums)
print(f"Duration: {time.time() - start_time:.2f} seconds")
