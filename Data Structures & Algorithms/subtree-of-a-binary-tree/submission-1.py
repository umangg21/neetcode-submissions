# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def sameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.res = []
        #check if root's any node similar to subtree

        def dfs(curr, toMatch):
            if not curr: 
                return
            if curr.val == toMatch.val:
                self.res.append(curr)

            dfs(curr.left, toMatch)
            dfs(curr.right, toMatch)
                
        dfs(root, subRoot)
        
        for i in self.res:
            if self.sameTree(i, subRoot):
                return True
        return False
