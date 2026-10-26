# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def countNodes(self, curr, maxSoFar):
        if not curr:
            return 0
        
        shouldAdd = 0
        if curr.val >= maxSoFar:
            shouldAdd = 1
            maxSoFar = curr.val
        
        return shouldAdd + self.countNodes(curr.left, maxSoFar) + self.countNodes(curr.right, maxSoFar)


    def goodNodes(self, root: TreeNode) -> int:
        if not self:
            return 0
  
        return self.countNodes(root, -math.inf)
        