# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # Time Complexity: O(n), where n is the total number of nodes
        # Space Complexity: O(h) where h is the height of the tree. If it's balanced tree, O(log(n))
        # if it's not balanced, then it's O(n)