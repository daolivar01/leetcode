class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize pointer to track the last unique element's index
        unique_idx = 0

        # Iterate through the list, starting at index 1
        for idx in range(1, len(nums)):
            # If current element is different from the last unique element
            if nums[idx] != nums[unique_idx]:
                # Move the unique pointer forward
                unique_idx += 1
                # Update the next unique position with the current element
                nums[unique_idx] = nums[idx]

        # Return the count of unique elements, which is unique_idx + 1
        return unique_idx + 1
