class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Problem Type: Sliding Window + Set for Duplicate Detection

        Approach:
            Maintain a sliding window of size at most `k` using a set to track
            recent elements within the window.

            Iterate through the list, adding elements to the window.
            If a duplicate is detected within the window, return True immediately.
            When the window size exceeds `k`, remove the oldest element to keep the window size fixed.

        Time Complexity: O(n)
            - Each element is added and removed from the set at most once.

        Space Complexity: O(min(n, k))
            - The size of the sliding window set is bounded by k or n.

        Args:
            nums (List[int]): Input list of integers.
            k (int): Maximum allowed index distance between duplicates.

        Returns:
            bool: True if any duplicate exists within `k` indices, False otherwise.
        """
        window = set()  # Tracks elements in current sliding window

        for i, num in enumerate(nums):
            if num in window:
                return True  # Duplicate found within window

            window.add(num)

            # Keep window size at most k by removing oldest element
            if i >= k:
                window.remove(nums[i - k])

        return False  # No duplicates found within distance k
