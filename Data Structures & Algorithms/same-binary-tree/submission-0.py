# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True, True
            elif not p and q:
                return False, False
            elif p and not q:
                return False, False
            
            left = dfs(p.left,q.left)
            right = dfs(p.right,q.right)

            flag = left[1] and right[1]
            if p.val == q.val and flag:
                return True, True
            else:
                return False, False

        return dfs(p,q)[0]