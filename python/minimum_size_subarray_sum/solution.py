class Solution:
    def minSubArrayLen(self, target, nums):
        """
        Problem Type: Sliding Window (Variable Size)

        Approach:
            Use a dynamic sliding window with two pointers:
              - Expand the window to the right by adding elements until the
                running sum is at least `target`.
              - Then shrink the window from the left to find the smallest valid window
                that satisfies the sum constraint.
            Keep track of the minimum window length found during this process.

        Time Complexity: O(n)
            - Each element is visited at most twice: once when added, once when removed.

        Space Complexity: O(1)
            - Uses only a few integer variables for pointers and sums.

        Args:
            target (int): The target sum the subarray should meet or exceed.
            nums (List[int]): List of positive integers.

        Returns:
            int: The length of the smallest subarray with sum ≥ target,
                 or 0 if no such subarray exists.
        """
        l = 0  # Left boundary of the sliding window
        r_sum = 0  # Running sum of current window
        min_len = float('inf')  # Track minimum valid window length

        for r in range(len(nums)):
            r_sum += nums[r]  # Expand window to the right

            # While current window sum meets or exceeds target,
            # try shrinking from the left to find smaller valid window
            while r_sum >= target:
                min_len = min(min_len, r - l + 1)
                r_sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len
