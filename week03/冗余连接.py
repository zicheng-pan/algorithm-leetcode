# linkfor:https://leetcode-cn.com/problems/redundant-connection/submissions/
from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.to = {}
        self.visited = []
        self.hascycle = False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for item in edges:
            self.n = max(item[0], item[1], self.n)
            list0 = self.to.get(item[0], [])
            list0.append(item[1])
            list1 = self.to.get(item[1], [])
            list1.append(item[0])
            self.to[item[0]] = list0
            self.to[item[1]] = list1
            self.visited = {item +1 :False for item in range(self.n)}
            hasCycle = self.dfs(item[0], 0)
            if hasCycle:
                return item
        return []

    def dfs(self, x, fa):
        hasCycle = False
        self.visited[x] = True
        for item in self.to[x]:
            if item == fa:
                continue
            if not self.visited[item]:
                self.dfs(item, x)
            else:
                hasCycle = True
        return hasCycle


solution = Solution()
print(str(solution.findRedundantConnection([[1,2],[1,3],[2,3]])))