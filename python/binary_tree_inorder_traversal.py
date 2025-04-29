class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        # Helper function to perform recursive inorder traversal
        def inorder(node, result):
            if node is None:
                return  # Base case: empty subtree
            inorder(node.left, result)      # Traverse left subtree
            result.append(node.val)         # Visit current node
            inorder(node.right, result)     # Traverse right subtree

        inorder(root, result)  # Start recursion from the root
        return result
