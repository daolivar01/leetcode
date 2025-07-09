class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Problem Type: Sliding window with dynamic size and duplicate detection

        Approach:
        Use a sliding window defined by two pointers (l, r) and a set to track
        unique characters in the current window. Expand the window by moving 'r'.
        When a duplicate is found, shrink the window from 'l' until the duplicate
        is removed. Track the maximum window size observed.

        Time Complexity: O(n), each character visited at most twice
        Space Complexity: O(min(n, m)), where m is the character set size (window size)

        Returns:
        int: Length of the longest substring without repeating characters
        """
        seen = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
