from typing import List


class Solution:
    def __init__(self):
        self.map = {}
        self.map[2] = "abc"
        self.map[3] = "def"
        self.map[4] = "ghi"
        self.map[5] = "jkl"
        self.map[6] = "mno"
        self.map[7] = "pqrs"
        self.map[8] = "tuv"
        self.map[9] = "wxyz"
        self.ans = []
        self.n = 0
        self.digists = None

    def letterCombinations(self, digits: str) -> List[str]:
        self.n = len(digits)
        self.digists = digits
        self.recur(0,"")
        return self.ans

    def recur(self,index, str):
        if index == self.n:
            self.ans.append(str)
            return

        for item in self.map[self.digists[index]]:
            index = index + 1
            self.recur(index, str + item)
            index = index - 1
