class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize a pointer to track the position where the next non-val element will go
        last_idx = 0

        # Iterate through the entire list to check each element
        for idx in range(0, len(nums)):
            # If the current element is not equal to val, it is a valid element
            if nums[idx] != val:
                # Place the valid element at the last_idx position
                nums[last_idx] = nums[idx]
                # Increment the last_idx to track the next position for valid elements
                last_idx += 1

        # Return the number of valid elements (i.e., new length of the list)
        return last_idx
