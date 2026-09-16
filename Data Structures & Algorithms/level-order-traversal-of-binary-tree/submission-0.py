# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [root]
        while queue:
            level = []
            curr_queue_len = len(queue)

            for i in range(curr_queue_len):
                curr = queue.pop(0)
                if not curr: return []
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            
            result.append(level)
                

        return result
        

        