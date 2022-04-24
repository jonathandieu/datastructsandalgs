# Leetcode (Easy)
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def max_profit(prices: list) -> int:

    max_profit = 0
    window_start = 0

    for window_end in range(1, len(prices)):
        # Find the cheapest buying day (update left)
        if prices[window_end] < prices[window_start]:
            window_start = window_end
        else:
            current_profit = prices[window_end] - prices[window_start]
            max_profit = max(current_profit, max_profit)
    return max_profit

# Driver Code
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Max Profit: {max_profit(prices)}")
    print(f"Expected: 5")