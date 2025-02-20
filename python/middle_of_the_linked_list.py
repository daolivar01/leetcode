class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize two pointers: slow and fast
        slow = head  # slow pointer moves one node at a time
        fast = head  # fast pointer moves two nodes at a time

        # Traverse the list: move slow by one node and fast by two nodes each iteration
        while fast and fast.next:
            slow = slow.next      # slow pointer moves one step
            fast = fast.next.next # fast pointer moves two steps

        # When the fast pointer reaches the end (or there is no next node), slow will be at the middle
        return slow
