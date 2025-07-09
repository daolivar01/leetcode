class Solution:
    def validPalindrome(self, s):
        """
        Problem Type: Two Pointers with Conditional Backtracking

        Approach:
            Use two pointers (left and right) to compare characters from both ends of the string.
            If characters match, continue inward. If a mismatch occurs, we can attempt to "repair" 
            the string by deleting either the left or right character, then checking if the remaining 
            substring is a palindrome.

            This leverages the fact that we are allowed at most one character deletion.

        Time Complexity: O(n)
            - In the worst case, we perform up to two O(n) checks: one for the original pass and
              one recursive-style check for each possible skip after a mismatch.

        Space Complexity: O(1)
            - Only uses constant extra space for pointers; no recursion stack due to iterative design.

        Args:
            s (str): The input string to validate.

        Returns:
            bool: True if the string can become a palindrome by deleting at most one character;
                  False otherwise.
        """

        def is_palindrome(l, r):
            """
            Helper function to check if s[l:r+1] is a palindrome using two pointers.

            Args:
                l (int): Left index
                r (int): Right index

            Returns:
                bool: True if the substring is a palindrome
            """
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
                # On mismatch, try deleting either character to attempt a valid palindrome
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)

        return True
