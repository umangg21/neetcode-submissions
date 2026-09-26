# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res = True

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            
            print(curr.val, left, right)
            
            diff = abs(left-right)
            isBal = True if diff <=1 else False

            self.res = self.res and isBal

            return 1 + max(left,right)

        dfs(root)
        return self.res
