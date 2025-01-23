class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow_ptr = head
        fast_ptr = head.next  # Initialize fast_ptr as the next node after head
        while fast_ptr and fast_ptr.next:  # Ensure fast_ptr and fast_ptr.next are valid
            if slow_ptr == fast_ptr:  # If the two pointers meet, there is a cycle
                return True
            slow_ptr = slow_ptr.next  # Move slow pointer by 1 step
            fast_ptr = fast_ptr.next.next  # Move fast pointer by 2 steps
        return False  # If no cycle is found
