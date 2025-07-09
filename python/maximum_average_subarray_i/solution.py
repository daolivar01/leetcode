class Solution:
    def findMaxAverage(self, nums, k):
        """
        Problem Type: Fixed-Size Sliding Window

        Approach:
            Calculate the sum of the first window of size `k`.
            Then slide the window through the array by subtracting the element 
            leaving the window and adding the new element entering the window.
            Track and update the maximum average encountered during the sliding process.

        Time Complexity: O(n)
            - Each element is added and removed exactly once from the window sum.

        Space Complexity: O(1)
            - Uses a fixed amount of extra space regardless of input size.

        Args:
            nums (List[int]): List of integers.
            k (int): Window size.

        Returns:
            float: The maximum average value of any contiguous subarray of length `k`.
        """
        total = sum(nums[:k])  # Initial window sum
        max_avg = total / k

        for i in range(k, len(nums)):
            # Slide the window by removing the leftmost element and adding the new element
            total += nums[i] - nums[i - k]
            max_avg = max(max_avg, total / k)

        return max_avg
