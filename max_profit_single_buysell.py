from typing import List

"""
Write a function to calculate the best profit that can be made from one purchase and one sale given a list of prices
Solution is O(n) time and constant space.
"""


def get_max_profit(prices: List[int]) -> int:
    """
    Return maximum profit from a single buy / sell
    :param prices: List of prices in time order
    :return: Maximum profit
    """
    if len(prices) < 2:
        return 0
    current_min = prices[0]
    max_profit_so_far = prices[1] - prices[0]
    for idx in range(1, len(prices)):
        max_profit_so_far = max(max_profit_so_far, prices[idx] - current_min)
        current_min = min(current_min, prices[idx])
    return max_profit_so_far


stock_prices = [16, 10, 15, 10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices))
