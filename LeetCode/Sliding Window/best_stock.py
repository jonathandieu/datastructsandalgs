class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        window_start = 0

        for window_end in range(len(prices)): # 0 - 5 range(6)
            current_profit = prices[window_end] - prices[window_start]
            if prices[window_end] < prices[window_start]:
                window_start = window_end
            else:
                max_profit = max(max_profit, current_profit)

        return max_profit