"""
Leetcode 191: Number of 1 Bits
Given an integer, return the number of ones in its binary reporesentation
"""

class Solution:
	def hammingWeight(self, n: int) -> int:
		answer = 0
		while n:
			answer += n % 2
			n //= 2
		return answer


# test cases
sol = Solution()
for i in range(100):
	assert format(i, 'b').count('1') == sol.hammingWeight(i)
