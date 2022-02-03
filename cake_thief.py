import unittest
from typing import List, Tuple, Union

"""
A twist on the unbounded knapsack problem:
Given an unlimited supply of cakes of different weights and values, return the maximum value that
can be obtained at a given capacity.
Two dynamic programming approaches: Top-down with memoization and bottom-up.
Bottom up worst case performance is O(K * N) where K is the capacity and N is the number of cake types. 
"""

Cake = Tuple[int, int]
Numeric = Union[int, float]


class CakeThief:

    """
    Bottom up and top down methods for cake thief problem
    """

    def __init__(self):
        self.memo = {}

    def max_value_top_down(self, cake_tuples: List[Cake], idx: int, capacity: int, value_so_far: int) -> Numeric:
        """
        Return maximum value to be obtained from cakes up to capacity
        :param cake_tuples: List of tuples of form (weight, value)
        :param idx: Current index of cake
        :param capacity: Room left in knapsack
        :param value_so_far: Value obtained so far
        :return: Maximum value
        """
        key = str((idx, capacity))
        if key in self.memo:
            return self.memo[key]

        if capacity <= 0 or idx >= len(cake_tuples):
            return value_so_far

        cake = cake_tuples[idx]
        if cake[0] == 0 and cake[1] > 0:
            return float("inf")

        max_value = 0
        while capacity >= 0:
            max_value = max(
                max_value,
                self.max_value_top_down(cake_tuples, idx + 1, capacity, value_so_far)
            )
            capacity -= cake[0]
            value_so_far += cake[1]

        self.memo[key] = max_value
        return max_value

    @staticmethod
    def max_value_bottom_up(cake_tuples: List[Cake], weight_capacity: int) -> Numeric:
        """
        Return maximum value to be obtained from cakes at capacity
        :param cake_tuples: List of tuples of form (weight, value)
        :param weight_capacity: Weight capacity of knapsack
        :return: Maximum value
        """
        max_value_at_weight = [0] * (weight_capacity + 1)

        for idx in range(1, len(max_value_at_weight)):
            max_cake_value = 0
            for cake in cake_tuples:
                if cake[0] == 0 and cake[1] > 0:
                    return float("inf")
                if cake[0] <= idx:
                    max_cake_value = max(
                        max_cake_value,
                        max_value_at_weight[idx - cake[0]] + cake[1]
                    )
            max_value_at_weight[idx] = max(
                max_value_at_weight[idx - 1],
                max_cake_value
            )
        return max_value_at_weight[weight_capacity]


def max_duffel_bag_value(cake_tuples: List[Cake], weight_capacity: int):
    """
    Return maximum value to be obtained from cakes at capacity
    :param cake_tuples: List of tuples of form (weight, value)
    :param weight_capacity: Weight capacity of knapsack
    :return: Maximum value
    """
    cake_tuples = [(weight, value) for weight, value in cake_tuples if value > 0]
    thief = CakeThief()
    return thief.max_value_bottom_up(cake_tuples, weight_capacity)


# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
