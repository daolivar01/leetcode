class Solution:
    def reverseString(self, s):
        """
        Problem Type: Two-pointer, in-place array reversal

        Approach:
        Use two pointers moving toward the center to swap characters in-place.
        This symmetric in-place swap pattern is optimal in time and space.

        Time Complexity: O(n), where n = len(s)
        Space Complexity: O(1), modifies the list in-place using constant extra space
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]  # Swap characters at symmetric positions
            l += 1
            r -= 1
