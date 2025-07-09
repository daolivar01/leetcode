class Solution:
    def isPalindrome(self, s):
        """
        Problem Type: Two Pointers + Character Filtering

        Approach:
            Use two pointers (`l` and `r`) to traverse the string from both ends. 
            Skip over any non-alphanumeric characters on either side, and compare the
            remaining characters in a case-insensitive manner.

            This approach avoids building a filtered copy of the string, keeping the solution in-place
            and space-efficient. It correctly handles strings with punctuation, whitespace, and mixed casing.

        Time Complexity: O(n)
            - Each character is visited at most once, due to the single pass of both pointers.

        Space Complexity: O(1)
            - Only uses constant extra space for pointers and character comparison; no extra data structures.

        Args:
            s (str): The input string to be checked for palindrome validity.

        Returns:
            bool: True if the string is a valid palindrome (ignoring non-alphanumeric and case),
                  False otherwise.
        """
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1

            # Skip non-alphanumeric characters from the right
            while l < r and not s[r].isalnum():
                r -= 1

            # Case-insensitive character comparison
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
