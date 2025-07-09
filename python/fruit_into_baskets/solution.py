class Solution:
    def totalFruit(self, fruits):
        """
        Problem Type: Sliding window with frequency map, at most k distinct elements (k=2)

        Approach:
        Use a sliding window with two pointers expanding right.
        Maintain a hash map counting fruit types in the current window.
        If the window contains more than two types, shrink from the left until valid.
        Track the maximum window size during traversal.

        Time Complexity: O(n), where n = len(fruits)
        Space Complexity: O(k), here k = 2 (max distinct fruit types in window)

        Returns:
        int: The length of the longest subarray containing at most two distinct fruit types
        """
        basket = {}  # Tracks count of each fruit type in current window
        l = 0
        max_len = 0

        for r, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
