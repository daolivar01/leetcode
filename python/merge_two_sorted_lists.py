class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Create a dummy node to act as the start of the merged list
        current = dummy  # This will track the last node in the merged list

        # Loop through both lists while neither is empty
        while list1 and list2:
            # If the value in list1 is smaller, add it to the merged list
            if list1.val < list2.val:
                current.next = list1  # Attach list1 node to the merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Attach list2 node to the merged list
                list2 = list2.next  # Move to the next node in list2
            current = current.next  # Move current to the next node

        # After the loop, one list might still have remaining elements
        # Attach the remaining part of either list1 or list2 (whichever is non-empty)
        current.next = list1 if list1 else list2

        # Return the merged list, starting from the node after dummy
        return dummy.next
