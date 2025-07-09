class Solution:
    def totalFruit(self, fruits):
        """
        Problem Type: Sliding Window with Frequency Map — At Most K Distinct Elements (k=2)

        Approach:
            Use a sliding window with two pointers (`l` and `r`) expanding to the right.
            Maintain a hash map (`basket`) counting the occurrences of each fruit type within the window.

            If the window contains more than two distinct fruit types, shrink it from the left
            until it contains at most two types again.

            Track and update the maximum window size observed during the traversal.

        Time Complexity: O(n)
            - Each element is added and removed from the window at most once.

        Space Complexity: O(k)
            - `basket` stores counts for up to k=2 fruit types.

        Args:
            fruits (List[int]): List representing fruit types on each tree.

        Returns:
            int: Length of the longest subarray with at most two distinct fruit types.
        """
        basket = {}  # Maps fruit type to its count within the current window
        l = 0  # Left pointer of sliding window
        max_len = 0  # Track max window size

        for r, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1  # Add current fruit to basket

            # If more than 2 distinct fruits, shrink window from left
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]  # Remove fruit type completely when count hits zero
                l += 1

            max_len = max(max_len, r - l + 1)  # Update max length

        return max_len
