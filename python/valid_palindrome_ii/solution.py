class Solution:
    def validPalindrome(self, s):
        """
        Returns True if the input string can be a palindrome after deleting at most one character.

        Uses the two-pointer technique to check for palindrome validity from both ends,
        allowing at most one mismatch (which can be resolved by skipping one character).

        Args:
            s (str): The input string.

        Returns:
            bool: True if a valid near-palindrome exists, False otherwise.
        """
        def is_palindrome(l, r):
            # Helper function to check if substring s[l:r+1] is a strict palindrome
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s) - 1

        # Two-pointer approach: scan from both ends toward the center
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # At most one mismatch allowed: skip left or right and validate the rest
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

        return True
