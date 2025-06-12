class Solution:
    def totalFruit(self, fruits):
        """
        Finds the length of the longest contiguous subarray (window) that contains at most
        two types of fruits. Each fruit type is represented by an integer.

        Uses a sliding window with a hash map to track the count of each fruit type 
        in the current window. The window expands right and shrinks from the left 
        when the fruit type count exceeds 2.

        Args:
            fruits: A list of integers representing types of fruits.

        Returns:
            The maximum number of fruits that can be picked (max window size with ≤ 2 types).
        """
        basket = {}    # Maps fruit type to its count in the current window
        left = 0       # Left boundary of the window
        max_len = 0    # Tracks the maximum number of fruits collected

        for right in range(len(fruits)):
            fruit = fruits[right]

            # Add current fruit to the basket
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1

            # Shrink window if we have more than 2 types of fruits
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            # Update max window size
            max_len = max(max_len, right - left + 1)

        return max_len
