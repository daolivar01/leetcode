class Solution:
    def reverseString(self, s):
        """
        Reverses a list of characters in-place.

        Problem Type: Two-pointer, in-place array manipulation
        Pattern: Symmetric element swapping using dual pointers

        Parameters:
        s (List[str]): A list of characters to be reversed in-place

        Returns:
        None: The input list is modified directly

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        l, r = 0, len(s) - 1

        # Two-pointer approach: move inward from both ends and swap
        while l < r:
            s[l], s[r] = s[r], s[l]  # symmetric swap
            l += 1
            r -= 1
