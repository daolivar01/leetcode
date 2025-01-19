class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If the strings have different lengths, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Dictionary to count occurrences of each character in both strings
        letter_count = {}

        # Traverse through both strings and update the letter count
        for i in range(len(s)):
            # Increase the count for character in string 's'
            letter_count[s[i]] = letter_count.get(s[i], 0) + 1
            # Decrease the count for character in string 't'
            letter_count[t[i]] = letter_count.get(t[i], 0) - 1

        # Check if all character counts are zero (indicating an anagram)
        for count in letter_count.values():
            if count != 0:
                return False

        # If all counts are zero, the strings are anagrams
        return True
