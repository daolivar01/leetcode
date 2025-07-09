class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Problem Type: Sliding window + set for duplicate detection

        Approach:
        Maintain a sliding window of size at most k using a set to track recent elements.
        If a duplicate appears within this window, return True immediately.
        Slide the window forward by removing the oldest element when the window exceeds size k.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(min(n, k)), size of the sliding window

        Returns:
        bool: True if any duplicate exists within k indices, else False
        """
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True  # Duplicate found in current window

            window.add(num)

            if i >= k:
                window.remove(nums[i - k])  # Slide window forward

        return False  # No duplicates found within distance k
