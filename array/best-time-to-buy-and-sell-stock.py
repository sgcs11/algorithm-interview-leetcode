import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for i, price in enumerate(prices):
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)

        return profit