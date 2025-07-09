class Solution:
    def checkInclusion(self, s1, s2):
        """
        Problem Type: Sliding window + frequency count (hash maps)

        Approach:
        Build a frequency map of s1, then slide a window of the same length over s2.
        Track the frequency of characters in the current window using a hash map.
        At each step, compare the two maps. A match indicates a valid permutation.

        Time Complexity: O(n), where n = len(s2)
        Space Complexity: O(1), since character set is limited (only lowercase letters)

        Returns:
        bool: True if any permutation of s1 exists as a substring in s2
        """
        from collections import defaultdict

        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        for c in s1:
            s1_count[c] += 1

        l = 0  # Left boundary of sliding window

        for r in range(len(s2)):
            window_count[s2[r]] += 1

            # Shrink window if it exceeds the length of s1
            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            # Check for permutation match
            if window_count == s1_count:
                return True

        return False
