class Solution:
    def groupAnagrams(self, strs):
        """
        Problem Type: Hash Map Bucketing + String Sorting

        Approach:
            Iterate through each word in the input list.
            For each word, sort its characters alphabetically to generate a key.
            Use a hash map (dictionary) where:
                - Key = sorted word (e.g., 'aet' from 'eat')
                - Value = list of words that share this sorted key (anagrams)

            If the key exists in the map, append the original word to its list.
            If not, initialize the list with that word.

            At the end, return all the values (lists of grouped anagrams).

        Time Complexity: O(n * k log k)
            - n = number of words
            - k = max length of a single word
            - Sorting each word takes O(k log k)

        Space Complexity: O(n * k)
            - Storing all the words in the dictionary buckets

        Args:
            strs (List[str]): List of input strings

        Returns:
            List[List[str]]: Groups of anagram words
        """
        anagram_map = {}

        for word in strs:
            # Sort the word to form the hashable key
            sorted_key = ''.join(sorted(word))

            # Check if the key is already in the map
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = []
            
            # Append the original word to the correct bucket
            anagram_map[sorted_key].append(word)

        # Return the grouped values
        return list(anagram_map.values())
