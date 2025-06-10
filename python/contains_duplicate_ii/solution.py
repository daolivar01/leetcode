class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Checks whether any duplicate exists in 'nums' such that the indices
        of the duplicates are at most 'k' apart.

        Uses a sliding window of size 'k' implemented via a set to track
        the most recent 'k' elements seen.

        Args:
            nums: List of integers to check.
            k: Maximum allowed index difference between duplicates.

        Returns:
            True if a duplicate exists within a distance of k, False otherwise.
        """
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                # Found a duplicate within the current window
                return True

            window.add(nums[i])

            # Ensure the window only holds at most 'k' recent elements
            if i >= k:
                window.remove(nums[i - k])

        # No nearby duplicates found
        return False
