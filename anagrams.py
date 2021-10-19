"""
Leetcode 49: Group Anagrams
Given an array of strings strs, group the anagrams together.
Straightforward approach using a defaultdict. I would have like to have used
itertools.groupby, but unless the input is sorted by the eventual key,
groupby does not keep the groups together.
This seemed like a simpler approach.
"""

from typing import List
from collections import defaultdict


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		groups = defaultdict(lambda: [])
		for word in strs:
			groups[''.join(sorted(word))].append(word)
		return [values for values in groups.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
