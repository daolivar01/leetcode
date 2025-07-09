class Solution:
    def removeDuplicates(self, nums):
        """
        Problem Type: Two Pointers, In-Place Overwrite for Deduplication

        Approach:
            Since the input list is sorted, duplicates appear consecutively.
            Use two pointers:
              - `write` tracks the position of the last unique element.
              - `read` scans through the list.
            When `nums[read]` differs from `nums[write]`, increment `write` and
            overwrite `nums[write]` with the new unique value found at `read`.

            This effectively shifts unique elements forward, removing duplicates
            without extra space.

        Time Complexity: O(n)
            - Single pass through the list.

        Space Complexity: O(1)
            - Modifies the list in-place with constant extra space.

        Args:
            nums (List[int]): Sorted list of integers with possible duplicates.

        Returns:
            int: The number of unique elements after duplicates removal.
        """
        if not nums:
            return 0

        write = 0  # Position of last unique element

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]  # Overwrite duplicate with unique element

        return write + 1  # Length of unique segment is last index + 1
