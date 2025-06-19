class Solution:
    def isPalindrome(self, s):
        """
        Determines if the given string is a valid palindrome, considering only alphanumeric characters
        and ignoring cases.

        Args:
            s (str): Input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Move left forward if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # Move right backward if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
