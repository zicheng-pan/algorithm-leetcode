# linkfor:https://leetcode-cn.com/problems/redundant-connection/submissions/
from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.to = {}
        self.visited = []
        self.hascycle = False
        self.du = {}

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        for item in edges:
            self.n = max(item[0], item[1], self.n)
            list0 = self.to.get(item[0], [])
            list0.append(item[1])
            self.to[item[0]] = list0
            self.visited = {item +1 :False for item in range(self.n)}
            hasCycle = self.dfs(edges[0][0])
            self.countdu()
            if hasCycle:
                for key in self.du.keys():
                    if self.du[key] > 1:

                return item
        return []

    def countdu(self):
        self.du = {}
        for item in self.to.keys():
            for temp in self.to[item]:
                self.du[temp] = self.du.get(temp,0) + 1


    def dfs(self, x):
        hasCycle = False
        self.visited[x] = True
        for item in self.to.get(x,[]):
            if not self.visited[item]:
                if self.dfs(item):
                    hasCycle = True
            else:
                hasCycle = True
        return hasCycle


solution = Solution()
print(str(solution.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])))