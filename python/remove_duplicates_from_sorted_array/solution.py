class Solution:
    def removeDuplicates(self, nums):
        """
        Problem Type: Two-pointer, in-place overwrite

        Approach:
        Use one pointer (read) to scan the sorted list and another (write) to track
        the last unique element's position. When a new unique value is found,
        overwrite the next write position. This removes duplicates in-place without extra space.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(1), in-place modification

        Returns:
        int: The length of the array after duplicates are removed
        """
        if not nums:
            return 0

        write = 0  # Points to last unique element

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]  # Overwrite duplicate with unique value

        return write + 1  # Length is index + 1
