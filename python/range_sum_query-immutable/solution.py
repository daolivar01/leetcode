class NumArray:
    def __init__(self, nums):
        """
        Problem Type: Prefix Sum Preprocessing

        Approach:
            Precompute a prefix sum array where each element at index `i`
            holds the sum of elements from index 0 to `i` in the original array.
            This allows constant-time range sum queries via subtraction.

        Time Complexity (init): O(n)
            - One pass to build the prefix sum array.

        Space Complexity: O(n)
            - Stores the prefix sum array of the same size as input.

        Args:
            nums (List[int]): Input list of integers.
        """
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        self.nums = prefix  # Store prefix sum for later queries

    def sumRange(self, left, right):
        """
        Returns the sum of elements between indices `left` and `right` (inclusive).

        Time Complexity: O(1)
            - Range sum computed in constant time using prefix differences.

        Args:
            left (int): Starting index of the range.
            right (int): Ending index of the range.

        Returns:
            int: The sum of the subarray nums[left:right + 1]
        """
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]
