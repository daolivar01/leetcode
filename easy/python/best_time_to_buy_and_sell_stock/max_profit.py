def maxProfit(self, prices):
    """
    Find maximum profit from buying and selling stock once.
    
    Args:
        prices: List of stock prices by day
        
    Returns:
        int: Maximum profit possible (0 if no profit can be made)
        
    Time: O(n), Space: O(1)
    """
    # Track the minimum price seen so far (best day to buy)
    min_price = float('inf')
    
    # Initialize to 0 (worst case: no profit)
    max_profit = 0

    # Scan through each day's price
    for price in prices:
        # If current price is lower than our minimum, update it
        if price < min_price:
            min_price = price
        
        # Calculate profit if we sold today (current price - minimum price so far)
        max_profit = max(price - min_price, max_profit)
    
    return max_profit
