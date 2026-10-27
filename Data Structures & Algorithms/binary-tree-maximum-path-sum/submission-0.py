# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -math.inf

        def path(curr):
            if not curr: return 0

            left = max(0, path(curr.left))
            right = max(0, path(curr.right))

            curr_sum= curr.val + left + right
            self.res = max(self.res, curr_sum) 

            return curr.val + max(left,right)
        

        path(root)
        return self.res
        