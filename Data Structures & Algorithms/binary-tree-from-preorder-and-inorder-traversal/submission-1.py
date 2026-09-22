# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: root, left, right
        #inorder: left, root, right
        
        #hash map for inorder to find mid quick

        indices = {}
        for i, item in enumerate(inorder):
            indices[item] = i

        self.root_index = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.root_index]

            mid_idx = indices[root_val]
            self.root_index += 1
            #find middle
            root = TreeNode(root_val)
            root.left = dfs(l, mid_idx - 1)
            root.right = dfs(mid_idx + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
