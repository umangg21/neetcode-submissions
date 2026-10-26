# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.res = None

        def visit(curr):

            if not curr:
                return
            
            if curr.left:
                visit(curr.left)
            
            self.count +=1
            if self.count == k:
                self.res = curr.val
            
            if curr.right:
                visit(curr.right)
        
        visit(root)
        return self.res