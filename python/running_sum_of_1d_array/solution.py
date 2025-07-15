class Solution:
    def runningSum(self, nums):
        """
        Problem Type: Prefix Sum / Running Total

        Approach:
            Iterate through the list, maintaining a cumulative running sum.
            At each index, store the current running sum in the result list.

            This builds a running sum array where each element represents the sum of
            all elements up to that index.

        Time Complexity: O(n)
            - Single pass through the input list.

        Space Complexity: O(n)
            - Output array of the same length as input.

        Args:
            nums (List[int]): Input list of integers.

        Returns:
            List[int]: Running sum array.
        """
        result = [0] * len(nums)  # Pre-allocate result list
        running_sum = 0  # Tracks cumulative sum

        for i in range(len(nums)):
            running_sum += nums[i]
            result[i] = running_sum  # Store running sum at index i

        return result
