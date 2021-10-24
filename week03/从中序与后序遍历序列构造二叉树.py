# linkfor: 从中序与后序遍历序列构造二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def __init__(self):
        self.postorder = []
        self.inorder = []

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.inorder = inorder
        return self.build(0, len(inorder) - 1, 0, len(postorder) - 1)

    def build(self, l1, r1, l2, r2):
        if l1 > r1:
            return None
        root = TreeNode(self.postorder[r2])
        mid = l1
        while self.inorder[mid] != root.val:
            mid = mid + 1

        root.left = self.build(l1, mid - 1, l2, l2 + (mid - 1 - l1))
        root.right = self.build(mid + 1, r1, l2 + (mid - 1 - l1) + 1, r2 - 1)
        return root


solution = Solution()
solution.buildTree([9, 3, 15, 20, 7]
                   , [9, 15, 7, 20, 3])
