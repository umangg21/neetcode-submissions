# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        start,end = 0, n - 1
        iomap = {e:i for i, e in enumerate(inorder)}
        self.idx = 0

        def dfs(start,end):
            if start > end or self.idx >=n: return None

            currVal = preorder[self.idx]
            rootNode = TreeNode(currVal) 
            idxOfIO = iomap[currVal]
            self.idx += 1

            rootNode.left = dfs(start, idxOfIO-1)
            rootNode.right = dfs(idxOfIO+1, end)

            return rootNode
        
        return dfs(start, end)



        