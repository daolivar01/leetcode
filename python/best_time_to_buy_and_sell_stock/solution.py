class Solution:
    def maxProfit(self, prices):
        """
        Problem Type: One-pass array scan for max difference (stock buy/sell)

        Approach:
        Track the minimum price seen so far while iterating through the prices.
        For each price, calculate potential profit by subtracting the minimum price.
        Update max profit whenever a higher profit is found.
        This greedy approach ensures O(n) time complexity with O(1) space.

        Time Complexity: O(n), where n = len(prices)
        Space Complexity: O(1), constant extra space used

        Returns:
        int: Maximum profit achievable by buying and selling once
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min price to current if lower
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate profit

        return max_profit
