class Solution:
    def maxArea(self, height):
        """
        Problem Type: Two Pointers — Container With Most Water

        Approach:
            Use two pointers initialized at both ends of the `height` array.
            At each step, calculate the area formed by the lines at the pointers:
              - Area = width * min(height[l], height[r])
            Update the maximum area found.

            Since the area is limited by the shorter line, move the pointer
            at the shorter boundary inward in hopes of finding a taller line
            that can increase the area.

        Time Complexity: O(n)
            - Each pointer moves inward at most n times.

        Space Complexity: O(1)
            - Uses a fixed number of variables regardless of input size.

        Args:
            height (List[int]): Heights of vertical lines.

        Returns:
            int: Maximum area of water container formed by any two lines.
        """
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            curr_height = min(height[l], height[r])
            curr_area = width * curr_height
            max_area = max(max_area, curr_area)

            # Move pointer at the shorter line inward to try for a taller boundary
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
