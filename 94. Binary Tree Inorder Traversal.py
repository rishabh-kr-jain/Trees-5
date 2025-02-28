#regular dfs
#space: O(h)
#time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal_list= list()
        self.dfs(root)
        return self.traversal_list
    def dfs(self,root):
        if root is None:
            return root
        self.dfs(root.left)
        self.traversal_list.append(root.val)
        self.dfs(root.right)
        return root
        
