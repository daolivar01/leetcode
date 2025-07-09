class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Problem Type: Sliding Window with Dynamic Size and Duplicate Detection

        Approach:
            Use two pointers (`l` and `r`) to define a sliding window over the string.
            Maintain a set (`seen`) of unique characters currently in the window.
            Expand the window by moving `r` forward, adding characters to the set.
            If a duplicate character is encountered (already in `seen`),
            shrink the window from the left by moving `l` forward and removing characters
            until the duplicate is removed.

            Throughout, track the maximum window size (longest substring without duplicates).

        Time Complexity: O(n)
            - Each character is visited at most twice: once when added, once when removed.

        Space Complexity: O(min(n, m))
            - Where n is the length of the string and m is the size of the character set.
            - The set stores unique characters in the current window.

        Args:
            s (str): Input string.

        Returns:
            int: Length of the longest substring without repeating characters.
        """
        seen = set()  # Set to track unique characters in current window
        l = 0  # Left pointer of sliding window
        max_len = 0  # Track max length of substring found

        for r in range(len(s)):
            # Shrink window from left if current character is a duplicate
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])  # Add current character to the set
            max_len = max(max_len, r - l + 1)  # Update max length if larger window found

        return max_len
