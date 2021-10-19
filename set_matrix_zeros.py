"""
Leetcode 73: Set matrix zeros
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's,
and return the matrix.
We use a marker 'zero' here. The drawback is that we need to iterate
the matrix twice.
"""

from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		for i, row in enumerate(matrix):
			for j, val in enumerate(row):
				if val == 0:
					for k in range(len(matrix[0])):
						row[k] = 0 if row[k] == 0 else 'zero'
					for k in range(len(matrix)):
						matrix[k][j] = 0 if matrix[k][j] == 0 else 'zero'
		for i, row in enumerate(matrix):
			for j, val in enumerate(row):
				if val == 'zero':
					row[j] = 0


sol = Solution()
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(f"Before {matrix}")
sol.setZeroes(matrix)
print(f"After {matrix}")
