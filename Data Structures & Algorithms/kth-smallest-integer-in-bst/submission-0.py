# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_nodes = []

        def in_order_traversal(curr):
            if not curr:
                return
            
            in_order_traversal(curr.left)
            ordered_nodes.append(curr.val) #visit
            in_order_traversal(curr.right)


        in_order_traversal(root)

        return ordered_nodes[k - 1]



        