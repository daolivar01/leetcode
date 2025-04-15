class MyHashSet(object):

    def __init__(self):
        # Initialize the hash set with a fixed size for the buckets (1000)
        # Each bucket will be a list, and all lists are initially empty.
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        """
        Add a key to the hash set.
        :type key: int
        :rtype: None
        """
        index = self._hash(key)

        # Only add the key if it's not already in the corresponding bucket
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key):
        """
        Remove a key from the hash set.
        :type key: int
        :rtype: None
        """
        index = self._hash(key)

        # Remove the key from the bucket if it exists
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        """
        Check if the key exists in the hash set.
        :type key: int
        :rtype: bool
        """
        index = self._hash(key)

        # Return True if the key exists in the corresponding bucket, otherwise False
        return key in self.buckets[index]

    def _hash(self, key):
        # Simple hash function: Compute the index by taking the modulus of the key with the size
        return key % self.size
