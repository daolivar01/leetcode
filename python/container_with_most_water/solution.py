class Solution:
    def maxArea(self, height):
        """
        Problem Type: Two-pointer, container with most water

        Approach:
        Use two pointers starting at both ends of the array.
        Calculate area between pointers and update maximum.
        Move the pointer at the shorter line inward, since the area
        is limited by the shorter boundary and moving the taller pointer won't help.

        Time Complexity: O(n), where n = len(height)
        Space Complexity: O(1), constant extra space

        Returns:
        int: Maximum area of water container formed by vertical lines
        """
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            curr_height = min(height[l], height[r])
            curr_area = width * curr_height
            max_area = max(max_area, curr_area)

            # Move pointer at the shorter line inward to try to find taller boundary
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
