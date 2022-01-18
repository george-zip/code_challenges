from typing import List


def make_suffix_array(s: str) -> List:
	d = {s[i:]: i for i in range(len(s))}
	return [d[key] for key in sorted(d.keys())]


def make_lcp_array(s: str, suffix_array: List[int]) -> List:
	lcp_array = [0] * len(s)
	for i in range(1, len(suffix_array)):
		for c1, c2 in zip(s[suffix_array[i - 1]:], s[suffix_array[i]:]):
			if c1 != c2:
				break
			lcp_array[i] += 1
	return lcp_array


def get_color(position: int, strings: List[str]) -> int:
	accumulated_position = 0
	for i, s in enumerate(strings):
		accumulated_position += len(s)
		if position < accumulated_position:
			return i
	return i


def k_longest_common_substring(strings: List[str], k: int) -> str:
	# find longest common substring that appears in 2 <= k <= n strings
	text = ""
	# Concatenate the strings together, joined by characters that
	# lexicographically less than strings contained. We can't guarantee
	# these won't be in any string unless we strip them out beforehand.
	for i, s in enumerate(strings):
		text += s + chr(i)
	# construct suffix and lcp arrays but ignore first n entries because they
	# will be the injected characters
	suffix_array = make_suffix_array(text)[len(strings):]
	lcp_array = make_lcp_array(text, suffix_array)


strings = ["ababbab", "baba", "booba"]
print(get_color(34, strings))
# print(make_suffix_array("ababba"))
