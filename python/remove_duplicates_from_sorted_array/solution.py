class Solution:
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the new length.

        Args:
            nums (List[int]): A sorted list of integers with possible duplicates.

        Returns:
            int: The length of the array with duplicates removed in-place.
        """
        if not nums:
            return 0

        slow = 0  # Points to the last unique element

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1  # Move slow pointer to next position
                nums[slow] = nums[fast]  # Overwrite duplicate with new unique value

        return slow + 1  # Length is last index + 1
