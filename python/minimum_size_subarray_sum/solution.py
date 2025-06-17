class Solution:
    def minSubArrayLen(self, target, nums):
        """
        Finds the minimal length of a contiguous subarray 
        for which the sum is greater than or equal to the target.

        Args:
            target: int - The target sum we want to reach or exceed.
            nums: List[int] - A list of positive integers.

        Returns:
            int - The length of the smallest such subarray, or 0 if none exists.
        """
        left = 0  # Left boundary of the sliding window
        r_sum = 0  # Running sum within the current window
        min_size = float('inf')  # Start with "infinite" window size

        for right in range(len(nums)):
            r_sum += nums[right]  # Expand the window to the right

            # Shrink the window as long as the sum is valid
            while r_sum >= target:
                min_size = min(min_size, right - left + 1)
                r_sum -= nums[left]
                left += 1

        # If no valid window was found, return 0
        return 0 if min_size == float('inf') else min_size
