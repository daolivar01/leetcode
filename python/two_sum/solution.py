class Solution:
    def twoSum(self, nums, target):
        """
        Problem Type: Hash Map Lookup / Single-Pass Array Scan

        Approach:
            Iterate over the array while maintaining a hash map (`num_to_index`) 
            that maps each number to its index.

            For each number `num` at index `idx`, compute its complement as 
            `target - num`. If the complement is already in the hash map, 
            that means we've seen the number that would complete the pair, 
            so return the stored index and the current index.

            This approach avoids nested loops and finds the solution in one pass.

        Time Complexity: O(n)
            - Each element is processed once, with constant-time hash table operations.

        Space Complexity: O(n)
            - In the worst case, we may store every number in the hash map.

        Args:
            nums (List[int]): The list of integers to search.
            target (int): The target sum.

        Returns:
            List[int]: Indices of the two numbers that add up to the target.
        """
        num_to_index = {}  # Maps a number to its index for fast complement lookup

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], idx]  # Found a valid pair

            # Store the number with its index for future lookups
            num_to_index[num] = idx

        return []  # Should not be reached if exactly one solution is guaranteed
