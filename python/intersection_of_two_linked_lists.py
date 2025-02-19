class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # Initialize two pointers, starting at the heads of both lists
        ptrA = headA
        ptrB = headB

        # Traverse both lists until the two pointers meet at the intersection or both reach None
        while ptrA != ptrB:
            # If ptrA reaches the end of List A, reset it to headB (the start of List B)
            # Otherwise, move to the next node in List A
            ptrA = ptrA.next if ptrA else headB

            # If ptrB reaches the end of List B, reset it to headA (the start of List A)
            # Otherwise, move to the next node in List B
            ptrB = ptrB.next if ptrB else headA

        # Return the intersection node, or None if no intersection exists
        return ptrA
