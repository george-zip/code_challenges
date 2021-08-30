"""
Leet Code Problem 8: String to Integer (atoi).
This approach uses the value of variables for the implicit state 
of the parsing. I would probably use a state machine if this 
were more complex.
"""

class Solution:
	def myAtoi(self, s: str) -> int:
		extracted = []
		sign = 0
		# extract valid digits, if any
		for c in s:
			if not sign:
				if c.isspace():
					continue
				elif c in ("+", "-"):
					sign = 1 if c == "+" else -1
				elif c.isnumeric():
					extracted.append(int(c))
					sign = 1
				else:
					break
			else:
				if c.isnumeric():
					extracted.append(int(c))
				else:
					break
		val = 0
		# generate integer result by multiplying digits 
		# by increasing powers of 10
		for i in range(len(extracted)):
			n = extracted.pop()
			val += n * 10 ** i
		val *= sign
		val = min(2 ** 31 - 1, val)
		val = max(-2 ** 31, val)
		return val



s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("-42"))
print(s.myAtoi("+42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))