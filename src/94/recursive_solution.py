# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []
        self._inorderTraversal(root, result)
        return result

    def _inorderTraversal(self, root, result):

        if not root:
            return

        self._inorderTraversal(root.left, result)
        result.append(root.val)
        self._inorderTraversal(root.right, result)
