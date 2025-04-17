class MyHashMap(object):

    def __init__(self):
        # Set the fixed size for the number of buckets
        self.size = 1000
        # Initialize the buckets as an array of None, each index can later hold a list
        self.buckets = [None] * self.size

    def put(self, key, value):
        """
        Insert a key-value pair into the HashMap.
        If the key already exists, update the value.
        """
        index = self._hash(key)
        # Create a bucket (list) if it doesn't exist
        if self.buckets[index] is None:
            self.buckets[index] = []
        # Check if key already exists, if so, update its value
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append the new [key, value] pair
        self.buckets[index].append([key, value])

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Returns -1 if the key does not exist.
        """
        index = self._hash(key)
        # If the bucket is empty, return -1
        if self.buckets[index] is None:
            return -1
        # Search the bucket for the key
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        # Key not found
        return -1

    def remove(self, key):
        """
        Remove the key-value pair associated with the given key.
        """
        index = self._hash(key)
        # If no bucket exists, nothing to remove
        if self.buckets[index] is None:
            return
        # Loop through the bucket using index so we can remove by index safely
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                del self.buckets[index][i]
                return

    def _hash(self, key):
        """
        Hash function to map the key to a bucket index.
        """
        return key % self.size
