# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(root, minv, maxv):
            if not root:
                return True

            if not (minv < root.val and maxv > root.val):
                return False

            return check(root.left, minv, root.val) and check(root.right, root.val, maxv)

        return check(root, -math.inf, math.inf)