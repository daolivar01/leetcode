class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        # Helper function to perform recursive postorder traversal
        def postorder(node, result):
            if node is None:
                return  # Base case: empty subtree
            postorder(node.left, result)     # Traverse left subtree
            postorder(node.right, result)    # Traverse right subtree
            result.append(node.val)          # Visit current node last

        postorder(root, result)  # Start recursion from the root
        return result
