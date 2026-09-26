# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res =[]

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)

            for i in range(qLen-1):
                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            lastNode = q.popleft()
            if lastNode:
                if lastNode.left: q.append(lastNode.left)
                if lastNode.right: q.append(lastNode.right)

                res.append(lastNode.val)
        
        return res

        