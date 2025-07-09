class Solution:
    def reverseString(self, s):
        """
        Problem Type: Two-Pointer, In-Place Reversal

        Approach:
            Use two pointers —`l` (left) starting at the beginning of the list,
            and `r` (right) starting at the end. Swap characters at `l` and `r`,
            then move both pointers inward until they meet or cross.

            This is a classic in-place reversal approach with optimal time and space efficiency.
            It works directly on the input list of characters, modifying it in-place.

        Time Complexity: O(n)
            - Each character is visited once during a single pass.

        Space Complexity: O(1)
            - Swaps are done in-place with only two pointers used.

        Args:
            s (List[str]): A list of characters to be reversed in-place.

        Returns:
            None: The input list `s` is modified in-place.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]  # Swap characters at symmetric positions
            l += 1
            r -= 1
