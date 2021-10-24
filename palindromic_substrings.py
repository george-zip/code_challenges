"""
Leetcode 5: Longest common palindromic substring
A brute force approach that checks every substring that shares the same beginning and ending character
I want to return to this problem and solve it using a suffix tree.
"""


def is_palindrome(potential):
	return potential == potential[::-1]


class Solution:

	def longestPalindromeNaive(self, s: str) -> str:
		"""
		Check every substring that has the same beginning and ending character and is longer than the current longest
		palindrome. This version is marginally faster than checking all substrings. It passes the Leetcode time limit
		but it's still O(n^3) because is_palindrome has to iterate the length of the string
		"""
		longest = s[0] if s else ""
		for i, _ in enumerate(s):
			j = i + len(longest)
			while j < len(s):
				if s[i] == s[j] and is_palindrome(s[i:j + 1]):
					longest = s[i:j + 1]
				j += 1
		return longest

	def longestPalindrome(self, s: str) -> str:
		return self.longestPalindromeNaive(s)


sol = Solution()
print(sol.longestPalindrome("aacabdkacaa"))
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ac"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome(""))
