# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,l,node):
        # check if node is a leaf node or not
        if not node:
            return 
        else:
            self.inorder(l,node.left)
            l.append(node.val)
            self.inorder(l,node.right)
        return l
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        lst=[]
        self.inorder(lst,root1)
        self.inorder(lst,root2)
        return sorted(lst)

        