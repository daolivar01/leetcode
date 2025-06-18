class Solution:
    def twoSum(self, numbers, target):
        """
        Given a sorted list of integers, returns the 1-based indices of the two numbers that add up to the target.

        Args:
            numbers (List[int]): A list of integers sorted in non-decreasing order.
            target (int): The target sum.

        Returns:
            List[int]: Indices (1-based) of the two numbers whose sum equals the target.
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices

            # Move the left or right pointer based on comparison
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []
