class Solution:
    def containsDuplicate(self, nums):
        """
        Problem Type: Hash Set Membership for Duplicate Detection

        Approach:
            Iterate through the list while maintaining a set of seen elements.
            For each number, check if it already exists in the set.
            If yes, return True immediately as a duplicate is found.
            Otherwise, add the number to the set and continue.

            This provides an efficient O(n) time solution, trading space for speed.

        Time Complexity: O(n)
            - Each element is checked once with O(1) average lookup in the set.

        Space Complexity: O(n)
            - In the worst case, all elements are unique and stored in the set.

        Args:
            nums (List[int]): List of integers to check for duplicates.

        Returns:
            bool: True if any duplicate exists, False otherwise.
        """
        seen = set()  # Tracks unique elements encountered so far

        for num in nums:
            if num in seen:
                return True  # Duplicate detected, early exit
            seen.add(num)

        return False  # No duplicates found after full traversal
