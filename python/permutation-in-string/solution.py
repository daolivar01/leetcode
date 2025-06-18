class Solution:
    def checkInclusion(self, s1, s2):
        """
        Returns True if s2 contains a permutation of s1.

        A permutation of s1 must have the same character frequencies.
        So we slide a window of length len(s1) over s2 and check if any
        substring matches s1's character frequency map.

        Args:
            s1 (str): The pattern string to check permutations of.
            s2 (str): The target string to search in.

        Returns:
            bool: True if any permutation of s1 exists as a substring in s2.
        """
        s1_count = {}
        window_count = {}

        # Build frequency map for s1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        left = 0  # Left boundary of the sliding window

        # Iterate through s2 using right boundary
        for right in range(len(s2)):
            # Add current character to the window count
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # Shrink the window if its size exceeds len(s1)
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1

            # Compare frequency maps when window size is valid
            if window_count == s1_count:
                return True

        return False
