# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = [root]
        right_side_result = []

        if not root:
            return right_side_result

        while queue:
            queue_len = len(queue)
            right_side_result.append(queue[queue_len - 1].val)

            for i in range(queue_len):
                curr = queue.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

        return right_side_result


        