class Solution:
    def twoSum(self, numbers, target):
        """
        Problem Type: Two Pointers on Sorted Array

        Approach:
            Use two pointers —`l` at the start and `r` at the end of the array. 
            At each step, compute the sum of numbers[l] + numbers[r]:
              - If the sum equals the target, return their 1-based indices.
              - If the sum is less than the target, move the left pointer forward to increase the sum.
              - If the sum is greater than the target, move the right pointer backward to decrease the sum.

            This approach relies on the input being sorted in non-decreasing order,
            which allows us to find the correct pair in linear time without using extra space.

        Time Complexity: O(n)
            - Each element is visited at most once by either pointer.

        Space Complexity: O(1)
            - Only two pointers are used; no extra data structures.

        Args:
            numbers (List[int]): A sorted list of integers.
            target (int): The target sum to find.

        Returns:
            List[int]: The 1-based indices of the two numbers that sum to the target.
                       Returns an empty list if no such pair exists (shouldn't happen per problem constraints).
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]  # Return 1-based indices as required

            elif curr_sum < target:
                l += 1  # Increase sum by moving left pointer right
            else:
                r -= 1  # Decrease sum by moving right pointer left

        return []  # Fallback, though per problem spec, solution always exists
