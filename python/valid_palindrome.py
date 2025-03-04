class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters on the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters on the right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters after lowercasing
            if s[left].lower() != s[right].lower():
                return False
            # Move pointers inward
            left += 1
            right -= 1

        return True
