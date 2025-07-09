class Solution:
    def validPalindrome(self, s):
        """
        Problem Type: Two-pointer with backtracking (at most one mismatch allowed)

        Approach:
        Use two pointers to compare characters from both ends. On mismatch,
        attempt to skip either the left or right character and check if the rest is a valid palindrome.
        At most one character may be deleted to satisfy the palindrome condition.

        Time Complexity: O(n), where n = len(s)
        Space Complexity: O(1), constant extra space used

        Edge case: Allows for exactly one "repair" via character deletion
        """

        def is_palindrome(l, r):
            # Standard two-pointer palindrome check for substring s[l:r+1]
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Try skipping either mismatched character (at most one allowed)
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)

        return True
