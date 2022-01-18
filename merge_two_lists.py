from typing import List


def merge_lists(list_of_lists: List[List]) -> List:
    result = []
    while li1 or li2:
        if not li2 or li1 and li1[0] < li2[0]:
            result.append(li1.pop(0))
        elif not li1 or li2 and li2[0] < li1[0]:
            result.append(li2.pop(0))
        elif li1[0] == li2[0]:
            result.append(li1.pop(0))
        print(li1, li2)
    return result


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 15, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))

my_list = []
alices_list = [1, 5, 8, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
