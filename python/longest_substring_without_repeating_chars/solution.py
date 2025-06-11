class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Finds the length of the longest substring without repeating characters.

        Uses a dynamic-sized sliding window with a set to maintain the current
        window of unique characters. The window expands by moving the right
        pointer and shrinks from the left when duplicates are encountered.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring with all unique characters.
        """
        seen = set()   # Stores characters currently in the window
        left = 0       # Left boundary of the sliding window
        max_len = 0    # Tracks the maximum length found

        for right in range(len(s)):
            # If the current character is a duplicate, shrink the window from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character to the window
            seen.add(s[right])

            # Update the max length of substring found so far
            max_len = max(max_len, right - left + 1)

        return max_len
