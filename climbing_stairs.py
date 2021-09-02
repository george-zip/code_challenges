"""
Leetcode 70: Climbing stairs 

Iterative and recursive approaches

A straightforward recursive approach without lru_cache
timed out in the Leetcode evaulation for n > 38 whereas 
the iterative approach beat 95% of the Python3 submissions.
Surprisingly, in my own timing tests diverge from these results:

~/codechallenges-1$ python climbing_stairs.py 
Iterative: 0.777899726992473
Recursive: 0.0002703469945117831

"""

from functools import lru_cache
import timeit

class Solution:
	cache = {
		1: 1,
		2: 2
	}

	def climbStairs(self, n: int) -> int:
		"""
		Memoized, iterative approach: Cache results to avoid 
		unecessary recalculation
		"""
		answer = 0
		if n > 0:
			if n in self.cache:
				answer = self.cache[n]
			else:
				for i in range(3, n):
					self.cache[i] = self.cache[i - 1] + self.cache[i - 2]
				answer = self.cache[n - 1] + self.cache[n - 2] 
		return answer

	@lru_cache(128)
	def climbStairsRecursive(self, n: int) -> int:
		"""
		Recursive approach
		Timed out without @lru_cache mechanism during Leetcode evaluation
		for n > 38
		"""
		answer = 0
		if n > 0:
			if n in (1, 2):
				answer = n
			else:
				answer = self.climbStairs(n - 1) + self.climbStairs(n - 2)
		return answer


sol = Solution()
assert sol.climbStairs(1) == 1
assert sol.climbStairs(2) == 2
assert sol.climbStairs(3) == 3
assert sol.climbStairs(4) == 5

# test difference in timing 

setup_code = """
from __main__ import Solution
sol = Solution()
"""

iterative_timing = timeit.timeit(
	stmt="sol.climbStairs(1000)", setup=setup_code, number=1000
)
print(f"Iterative: {iterative_timing}")

recursive_timing = timeit.timeit(
	stmt="sol.climbStairsRecursive(1000)", setup=setup_code, number=1000
)
print(f"Recursive: {recursive_timing}")