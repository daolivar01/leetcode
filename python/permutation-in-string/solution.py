class Solution:
    def checkInclusion(self, s1, s2):
        """
        Problem Type: Sliding Window + Frequency Count (Hash Maps)

        Approach:
            Use a fixed-size sliding window over `s2` equal to the length of `s1`.
            Maintain frequency counts of characters within the window (`window_count`) 
            and the target string `s1` (`s1_count`).

            For each character added to the window, update the frequency.
            When the window size exceeds `len(s1)`, remove the leftmost character's count.

            At each step, compare the frequency maps. If they match, a permutation
            of `s1` exists as a substring of `s2`.

        Time Complexity: O(n), where n = len(s2)
            - Each character is visited once when added and once when removed from the window.

        Space Complexity: O(1)
            - The character set is limited (lowercase English letters),
              so frequency maps have bounded size.

        Args:
            s1 (str): The string whose permutations we want to find.
            s2 (str): The string to search within.

        Returns:
            bool: True if any permutation of `s1` is a substring of `s2`, False otherwise.
        """
        from collections import defaultdict

        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        # Build frequency map for s1
        for c in s1:
            s1_count[c] += 1

        l = 0  # Left index of the sliding window

        for r in range(len(s2)):
            window_count[s2[r]] += 1  # Add current character to the window

            # If window size exceeds s1 length, shrink from the left
            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]  # Clean up zero-count entries
                l += 1

            # Check if current window matches s1's frequency map
            if window_count == s1_count:
                return True

        return False
