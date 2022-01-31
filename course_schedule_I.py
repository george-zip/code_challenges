from collections import defaultdict
from typing import List, Dict, Set

"""
Leetcode 207: Course schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take 
course a.
This does recursive DFS on the prerequisites for each course, keeping a trail of breadcrumbs to check for cycles
and also keeping track of courses for which we know the prerequisites can be satisfied. The latter allows us to 
visit each vertex only once.
Worst case time complexity O(n + m) where n = len(prerequisites) and m = len(numCourses)
"""


def is_cyclic(course: int, breadcrumbs: List[bool],
              prerequisites_map: Dict[int, List[int]], visited: Set[int]) -> bool:
    """
    Return true if prerequisites for course contain a cycle
    :param course: course number
    :param breadcrumbs: courses already encountered
    :param prerequisites_map: courses -> prerequisites
    :param visited: Set of courses that have already been traversed and so can be skipped if encountered
    :return: True if there is a cycle, False otherwise
    """
    if breadcrumbs[course]:
        # cycle
        return True
    if course in visited:
        # we've already confirmed this course path is satisfied
        return False
    breadcrumbs[course] = True
    if course in prerequisites_map:
        for pr in prerequisites_map[course]:
            if is_cyclic(pr, breadcrumbs, prerequisites_map, visited):
                return True
    breadcrumbs[course] = False
    return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Return True if prerequisites can be satisfied for all courses
        :param numCourses: Total courses in range [0, numCourses - 1]
        :param prerequisites: List of prerequisites in form [course : prerequisite]
        :return: True if no cycles, False otherwise
        """
        prerequisites_map = defaultdict(lambda: [])
        for pr in prerequisites:
            prerequisites_map[pr[0]].append(pr[1])
        breadcrumbs = [False] * numCourses
        visited = set()
        for course in range(numCourses):
            if is_cyclic(course, breadcrumbs, prerequisites_map, visited):
                return False
            visited.add(course)
        return True


def run_test(numCourses: int, prerequisites: List[List[int]]) -> bool:
    sol = Solution()
    return sol.canFinish(numCourses, prerequisites)


def test_basic():
    assert run_test(2, [[1, 0]])


def test_three_courses():
    assert run_test(3, [[1, 0], [2, 1]])


def test_three():
    assert run_test(4, [[1, 0], [2, 0], [3, 1], [3, 2]])


def test_no_way_home():
    assert run_test(2, [[1, 0], [0, 1]]) is False


def test_empty():
    assert run_test(1, [])


def test_longer():
    assert run_test(
        20,
        [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
    ) is False


def test_cycle():
    assert run_test(3, [[1, 0], [1, 2], [0, 1]]) is False
