# linkfor: https://leetcode-cn.com/problems/surrounded-regions/
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        move_x = [-1, 0, 0, 1]
        move_y = [0, -1, 1, 0]

        if not board:
            return

        n = len(board)
        m = len(board[0])
        self.n = n
        self.m = m
        self.board = board

        queue = []
        self.ans = []
        for index_m in range(m):
            if board[0][index_m] == 'O':
                queue.append([0, index_m])
                self.ans.append([0, index_m])

            if board[n - 1][index_m] == 'O':
                queue.append([n-1, index_m])
                self.ans.append([n-1, index_m])

        for index_n in range(n):
            if board[index_n][0] == 'O':
                queue.append([index_n, 0])
                self.ans.append([index_n, 0])

            if board[index_n][m - 1] == 'O':
                queue.append([index_n, m - 1])
                self.ans.append([index_n, m - 1])

        while queue:
            x, y = queue.pop()
            for item in range(len(move_x)):
                x_temp = x + move_x[item]
                y_temp = y + move_y[item]
                if self.valid(x_temp,y_temp):
                    queue.append([x_temp,y_temp])
                    self.ans.append([x_temp,y_temp])

        for x in range(n):
            for y in range(m):
                if [x,y] not in self.ans and self.board[x][y] == 'O':
                    self.board[x][y] = 'X'

        return self.board





    def valid(self,x,y):
        return x>= 0 and x < self.n and y >=0 and y < self.m and self.board[x][y] == 'O' and [x,y] not in self.ans


solution = Solution()
print(solution.solve(
[["O","O"],["O","O"]]))