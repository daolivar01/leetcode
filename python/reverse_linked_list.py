class Solution(object):
    def reverseList(self, head):
        """
        Reverses a singly linked list.
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous = None  # Initialize previous to None (this will be the new tail)
        current = head  # Start from the head of the list

        # Traverse the list
        while current:
            nextNode = current.next  # Temporarily store the next node
            current.next = previous  # Reverse the current node's pointer
            previous = current  # Move previous to the current node
            current = nextNode  # Move to the next node

        return previous  # Return the new head (previous points to the reversed head)
