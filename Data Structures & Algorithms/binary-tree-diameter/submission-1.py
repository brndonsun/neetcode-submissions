# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def max_length(root):
            if not root:
                return 0

            left = max_length(root.left)
            right = max_length(root.right)

            self.max_diameter = max(self.max_diameter, right + left)
            return 1 + max(left, right)

        max_length(root)
        return self.max_diameter
