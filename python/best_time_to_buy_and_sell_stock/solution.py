class Solution:
    def maxProfit(self, prices):
        """
        Problem Type: One-Pass Array Scan for Maximum Difference (Stock Buy/Sell)

        Approach:
            Iterate through the list of prices while tracking the minimum price observed so far.
            At each price, calculate the potential profit by subtracting the minimum price.
            Update the maximum profit whenever a higher profit is found.

            This greedy strategy ensures we buy at the lowest price before selling at a higher price,
            with a single pass through the data.

        Time Complexity: O(n)
            - Single pass through the prices list.

        Space Complexity: O(1)
            - Uses only constant extra space for tracking min price and max profit.

        Args:
            prices (List[int]): List of stock prices by day.

        Returns:
            int: The maximum profit possible from one buy and one sell transaction.
        """
        min_price = prices[0]  # Track minimum price seen so far
        max_profit = 0  # Track maximum profit observed

        for price in prices:
            if price < min_price:
                min_price = price  # Found new minimum price
            else:
                # Calculate potential profit and update max profit if better
                max_profit = max(max_profit, price - min_price)

        return max_profit
