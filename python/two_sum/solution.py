class Solution:
    def twoSum(self, nums, target):
        """
        Problem Type: Hash map lookup / Single-pass array scan

        Approach:
        Iterate through the list while maintaining a hash map of values to their indices.
        For each number, calculate its complement (target - num) and check if it's already in the map.
        If found, return the pair of indices. Otherwise, store the current number and index.

        This avoids nested loops and solves the problem in linear time by trading space.

        Time Complexity: O(n), where n is the number of elements in 'nums'
        Space Complexity: O(n), for storing the hash map
        """
        num_to_index = {}  # Maps number to its index for constant-time complement lookup

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], idx]  # Found valid pair

            # Store the number and its index for future lookup
            num_to_index[num] = idx

        return []  # No valid pair found
