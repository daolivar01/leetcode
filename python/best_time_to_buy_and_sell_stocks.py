class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]  # Initialize minPrice with the first price
        maxProfit = 0  # Initialize maxProfit to 0

        # Iterate through the prices starting from the second price
        for price in prices[1:]:
            if price < minPrice:  # Update minPrice if the current price is lower
                minPrice = price
            else:
                # Calculate profit if selling at the current price is profitable
                if price - minPrice > maxProfit:
                    maxProfit = price - minPrice  # Update maxProfit with the best profit so far

        return maxProfit  # Return the maximum profit found
