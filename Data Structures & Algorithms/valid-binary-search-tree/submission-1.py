# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #base case
        
        def recurse(curr, min_bound, max_bound):
            if not curr:
                return True

            if curr.val <= min_bound: return False
            if curr.val >= max_bound: return False

            return recurse(curr.left, min_bound, curr.val) and             recurse(curr.right ,curr.val, max_bound)

            

        
        return recurse(root, -float('inf'), float('inf'))