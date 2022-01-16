from typing import List

"""
Reverse list of characters separated by space (or words) in place
"""


def reverse_list(li: List, start=0, end=None) -> None:
    """
    Reverse subset of list in place
    :param li: List to be reversed
    :param start: Starting index
    :param end: Ending index (inclusive)
    :return: None
    """
    i = start
    j = end if end else len(li) - 1
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1


def reverse_words(words: List) -> None:
    """
    Reverse the order of the words in place.
    :param words: List of characters separated by space (for example ['h','i',' ','t','h','e','r','e']
    :return: None
    """
    reverse_list(words)
    start = 0
    for idx, c in enumerate(words):
        if c == ' ':
            reverse_list(words, start, idx - 1)
            start = idx + 1
    reverse_list(words, start)


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']

print(f"Before: {''.join(message)}")
reverse_words(message)
print(f"After: {''.join(message)}")
