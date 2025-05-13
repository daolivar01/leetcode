class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = 0  # Sum of the current window of size k
        max_average = float('-inf')  # Initialize to the lowest possible value
        window_start = 0  # Start index of the sliding window

        for window_end in range(len(nums)):
            window_sum += nums[window_end]  # Expand the window to the right

            # Check if we've hit the window size of k
            if window_end >= k - 1:
                # Update the maximum average found so far
                max_average = max(max_average, float(window_sum) / k)

                # Slide the window forward: subtract the element going out
                window_sum -= nums[window_start]
                window_start += 1

        return max_average
