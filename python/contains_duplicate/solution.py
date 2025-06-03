class Solution:
    def containsDuplicate(self, nums):
        """
        Checks if the list 'nums' contains any duplicate elements.

        Uses a set to keep track of seen numbers, returning True as soon as
        a duplicate is detected to minimize time.

        Args:
            nums: List of integers to check for duplicates.

        Returns:
            True if any duplicate exists, False otherwise.
        """
        seen = set()  # To store numbers we've seen so far

        for num in nums:
            if num in seen:
                # Duplicate found
                return True
            seen.add(num)

        # No duplicates found after checking all elements
        return False
