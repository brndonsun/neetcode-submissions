class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(prices[sell] - prices[buy], max_profit)
                sell += 1
            else:
                buy = sell
                sell += 1
        return max_profit