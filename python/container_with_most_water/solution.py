class Solution:
    def maxArea(self, height):
        """
        Calculates the maximum area of water a container can hold given the heights of vertical lines.

        Uses the two-pointer technique to scan from both ends inward, always moving the pointer
        pointing to the shorter line, since the area is limited by the shorter boundary.

        Args:
            height (List[int]): List of non-negative integers representing vertical line heights.

        Returns:
            int: The maximum area of water that can be contained.
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        # Two-pointer approach: check all possible widest containers, narrowing inward
        while left < right:
            # Calculate the current container's area
            width = right - left
            curr_height = min(height[left], height[right])
            curr_area = width * curr_height

            # Update max_area if this one is bigger
            max_area = max(max_area, curr_area)

            # Move the pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
