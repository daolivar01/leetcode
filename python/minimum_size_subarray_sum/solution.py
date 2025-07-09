class Solution:
    def minSubArrayLen(self, target, nums):
        """
        Problem Type: Sliding window (variable size)

        Approach:
        Use a dynamic sliding window to track a running sum. Expand the window to the right
        until the sum meets or exceeds the target. Then, shrink from the left to find the
        smallest valid window. Update the minimum length whenever a valid window is found.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(1), uses only constant extra space

        Returns:
        int: Length of the smallest subarray with sum ≥ target, or 0 if no such subarray exists
        """
        l = 0
        r_sum = 0
        min_len = float('inf')

        for r in range(len(nums)):
            r_sum += nums[r]  # Expand window to include nums[r]

            # Shrink window while valid to find the minimal length
            while r_sum >= target:
                min_len = min(min_len, r - l + 1)
                r_sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len
