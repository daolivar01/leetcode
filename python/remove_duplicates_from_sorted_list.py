class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty, there's nothing to remove, so return the head as is
        if head is None:
            return head

        # Start with the first node
        current = head

        # Traverse the list until the second-to-last node
        while current.next:
            # If the current node's value equals the next node's value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next

        # Return the modified list, starting from the head
        return head
