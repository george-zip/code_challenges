from typing import List

"""
Function for finding the index of the rotation point of a sorted list.
This version uses binary search and gives us O(log n) worst case performance
"""


def find_rotation_point(word_list: List[str]) -> int:
    """
    Find rotation point of sorted list
    :param word_list: List of words
    :return: Index of rotation point
    """
    if len(word_list) < 2:
        return 0
    floor_idx = -1
    ceiling_idx = len(word_list)
    first_word = word_list[0]
    if word_list[-1] > first_word:
        return 0
    while floor_idx < ceiling_idx:
        midpoint_idx = floor_idx + (ceiling_idx - floor_idx) // 2
        if word_list[midpoint_idx] >= first_word:
            floor_idx = midpoint_idx
        else:
            ceiling_idx = midpoint_idx
        if floor_idx + 1 == ceiling_idx:
            return ceiling_idx
    return midpoint_idx


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'yas',
    'zebra',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'coffee',
    'dogs',
    'engender',
    'karpatka',
    'leper',
    'money',
    'nana',
    'nba',
    'othellolagkage'
]

print(find_rotation_point(words))
