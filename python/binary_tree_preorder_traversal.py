class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        # Helper function to perform recursive preorder traversal
        def preorder(node, result):
            if node is None:
                return  # Base case: empty subtree
            result.append(node.val)         # Visit current node first
            preorder(node.left, result)     # Traverse left subtree
            preorder(node.right, result)    # Traverse right subtree

        preorder(root, result)  # Start recursion from the root
        return result
