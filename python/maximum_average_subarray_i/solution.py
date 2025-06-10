class Solution:
    def findMaxAverage(self, nums, k):
        """
        Finds the maximum average of any contiguous subarray of length 'k' in 'nums'.

        Uses a sliding window to efficiently track the sum of the current subarray.
        Updates the maximum average as the window moves forward.

        Args:
            nums: List of integers.
            k: Size of the subarray to consider.

        Returns:
            The maximum average (float) of any subarray of length k.
        """
        total = sum(nums[:k])  # Sum of the first window
        max_avg = total / float(k)

        for i in range(k, len(nums)):
            # Slide the window by removing the leftmost element and adding the new one
            total += nums[i] - nums[i - k]
            max_avg = max(max_avg, total / float(k))

        return max_avg
