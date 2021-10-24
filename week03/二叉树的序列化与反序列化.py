# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.seq = []
        self.current = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        self.dfs(root)
        return ",".join(self.seq)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.seq = data.split(",")
        self.current = 0
        return self.restore()

    def restore(self):

        if self.seq[self.current] == 'null':
            self.current = self.current+1
            return None
        root = TreeNode(self.seq[self.current])
        self.current = self.current+1
        root.left = self.restore()
        root.right = self.restore()
        return root


    def dfs(self, root):
        if root == None:
            self.seq.append('null')
            return
        self.seq.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize( [1,2,3,None,None,4,5]))