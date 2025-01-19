class Solution(object):
    def containsDuplicate(self, nums):
        """
        Checks if the list contains any duplicates.
        
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()  # Set to track numbers we've seen
        for num in nums:
            if num in seen:  # If we've seen the number, it's a duplicate
                return True
            seen.add(num)  # Otherwise, add the number to the set
        return False  # No duplicates found
