class Solution:
    def containsDuplicate(self, nums):
        """
        Problem Type: Hash set membership for duplicate detection

        Approach:
        Iterate through the list, using a set to track seen elements.
        Return True immediately upon detecting a duplicate.
        This approach achieves O(n) time complexity with O(n) extra space.

        Time Complexity: O(n), where n = len(nums)
        Space Complexity: O(n), for the hash set storage

        Returns:
        bool: True if any duplicate exists, False otherwise
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True  # Early exit on duplicate detection
            seen.add(num)

        return False  # No duplicates found
