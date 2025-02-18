class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]  # The head node of the linked list.
        :type val: int  # The value to remove from the linked list.
        :rtype: Optional[ListNode]  # The new head of the modified linked list.
        """
        # Create a dummy node that points to the head of the list
        # This helps handle edge cases like removing the head node itself
        dummy = ListNode()
        dummy.next = head

        # Initialize the current pointer to the dummy node
        current = dummy

        while current.next:
            # Check if the next node's value matches the value to remove
            if current.next.val == val:
                # If it matches, skip the current node by pointing to the next node
                current.next = current.next.next
            else:
                # If it doesn't match, move the current pointer to the next node
                current = current.next

        # Return the new head of the linked list (which is dummy.next)
        return dummy.next

