# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: TreeNode) -> int:
            nonlocal res # this allows modification to the res outside the dfs method
            # basically, the dfs will return the height, 
            # and in the logic we update the longest diameter
            if not root:
                return -1 # if the node doesn't exist, we are assuming the height is -1
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, 2 + left + right) # diameter will be 2 + height of left + height of right
            # 2 is the two edges from the root node

            return 1 + max(left, right)
        
        dfs(root)
        return res