class Solution:
    def isPalindrome(self, s):
        """
        Problem Type: Two-pointer, filtered character comparison

        Approach:
        Use two pointers to traverse the string from both ends.
        Skip non-alphanumeric characters and compare the remaining ones in a case-insensitive way.
        If all such character pairs match, the string is a valid palindrome.

        This avoids extra space by skipping characters in-place during traversal.

        Time Complexity: O(n), where n = len(s)
        Space Complexity: O(1), constant space usage (ignores input size)
        """
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
