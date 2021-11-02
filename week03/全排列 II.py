from typing import List


class Solution:
    def __init__(self):
        self.ans = set()
        self.a = []
        self.isUsd = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.isUsd = [False for _ in range(len(nums))]
        self.recur(nums, 0)
        return [eval(item) for item in self.ans]

    def recur(self, nums, index):
        if index == len(nums):
            self.ans.add(str(self.a.copy()))
            return

        for item in range(len(nums)):
            if not self.isUsd[item]:
                self.a.append(nums[item])
                self.isUsd[item] = True
                self.recur(nums, index + 1)
                self.isUsd[item] = False
                self.a.pop()
