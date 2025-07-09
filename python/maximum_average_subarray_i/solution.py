class Solution:
    def findMaxAverage(self, nums, k):
        """
        Problem Type: Fixed-size sliding window

        Approach:
        Compute the sum of the first window of size k. Then slide the window
        across the array by subtracting the leftmost element and adding the
        new rightmost element. Track the maximum average seen during this process.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(1), uses constant extra space

        Returns:
        float: Maximum average of any contiguous subarray of length k
        """
        total = sum(nums[:k])
        max_avg = total / k

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]  # Update window sum
            max_avg = max(max_avg, total / k)

        return max_avg
