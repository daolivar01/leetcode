class Solution:
    def twoSum(self, numbers, target):
        """
        Problem Type: Two-pointer on sorted array

        Approach:
        Use two pointers starting at the beginning and end of the sorted list.
        Calculate the sum of values at the pointers. If it matches target, return indices.
        If the sum is less than target, move left pointer forward to increase sum.
        If the sum is more than target, move right pointer backward to decrease sum.
        This exploits the sorted property to find the pair in O(n) time without extra space.

        Time Complexity: O(n), where n = len(numbers)
        Space Complexity: O(1), constant space used

        Returns:
        List[int]: 1-based indices of the two numbers adding up to target
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]  # 1-based indices

            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return []
