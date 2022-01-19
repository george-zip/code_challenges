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
    current_min = 0
    current_max = 0
    max_profit_so_far = 0
    for idx, px in enumerate(prices):
        if idx == 0:
            current_min = px
            current_max = px
        else:
            if px < current_min:
                max_profit_so_far = max(max_profit_so_far, current_max - current_min)
                current_min = px
                current_max = px
            elif px > current_max:
                current_max = px
    return max(max_profit_so_far, current_max - current_min)


stock_prices = [16, 10, 15, 10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices))
