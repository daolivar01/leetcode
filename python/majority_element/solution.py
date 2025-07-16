class Solution:
    def majorityElement(self, nums):
        """
        Problem Type: Boyer-Moore Voting Algorithm (Greedy / Linear Scan)

        Approach:
            Since the majority element is guaranteed to appear more than ⌊n / 2⌋ times,
            we can track a single candidate while traversing the array.

            Maintain a `candidate` and a `count`. 
            - If `count` is 0, set the current element as the new candidate.
            - If the current element equals the candidate, increment `count`.
            - Otherwise, decrement `count`.

            This greedy cancel-out approach guarantees that the true majority element
            will remain by the end of the traversal.

        Time Complexity: O(n)
            - Single pass over the array.

        Space Complexity: O(1)
            - Uses only constant extra space.

        Args:
            nums (List[int]): List of integers with guaranteed majority element.

        Returns:
            int: The majority element.
        """
        candidate = 0
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            elif n == candidate:
                count += 1
            else:
                count -= 1

        return candidate
