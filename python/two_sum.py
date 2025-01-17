class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds two numbers in the list 'nums' that add up to the 'target' and returns their indices.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_numbers = {}  # Store numbers and their indices
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement of the current number
            if complement in seen_numbers:  # If complement exists, we have found a match
                return [seen_numbers[complement], index]  # Return indices of complement and current number
            seen_numbers[num] = index  # Store the current number and its index in the dictionary
        return []  # Return an empty list if no solution is found

