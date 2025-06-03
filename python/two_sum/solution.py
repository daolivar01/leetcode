class Solution:
    def twoSum(self, nums, target):
        """
        Finds two indices in 'nums' such that the numbers at those indices add up to 'target'.

        Uses a hash map to store numbers seen so far and their indices, 
        allowing for O(n) time complexity by checking complements in one pass.

        Args:
            nums: List of integers to search.
            target: Target sum to find.

        Returns:
            List of indices of the two numbers adding up to target.
            Returns an empty list if no valid pair is found.
        """
        num_to_index = {}  # Map from number to its index

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # Found the pair that sums to target
                return [num_to_index[complement], idx]
            # Store the current number's index for future complement checks
            num_to_index[num] = idx

        # No pair found that sums to target
        return []
