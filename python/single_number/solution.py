class Solution:
    def singleNumber(self, nums):
        """
        Problem Type: Hash Map Frequency Count

        Problem:
            Given a list of integers where every element appears twice except one,
            return the element that appears only once.

        Approach:
            - Use a hash map (dictionary) to count occurrences of each number.
            - Iterate over the map to find the number with count == 1.

        Time Complexity: O(n)
            - One pass to count, one pass to find the single number.

        Space Complexity: O(n)
            - Extra space for hash map storing up to n/2 + 1 unique keys.

        Args:
            nums (List[int]): List of integers where one element appears only once.

        Returns:
            int: The single number that appears only once.
        """
        num_counts = {}
        for n in nums:
            num_counts[n] = num_counts.get(n, 0) + 1
        
        for num, count in num_counts.items():
            if count == 1:
                return num
