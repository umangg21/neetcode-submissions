# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []

        def dfs(curr):
            if curr is None: 
                self.res.append('N')
                return 

            self.res.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        final = ",".join(map(str, self.res))

        return final
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = data.split(",")
        
        def dfs(nums):
            val = nums.pop(0)
 

            if val == 'N':
                return None
            
            root = TreeNode(int(val))
            root.left = dfs(nums)
            root.right = dfs(nums)

            return root
        
        res = dfs(nums)
        return res



        
