# linkfor: https://leetcode-cn.com/problems/two-sum/description/
# 用数组和链表实现两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(enumerate(nums),key = lambda x: x[1])
        idx = [i[0] for i in sorted_nums]

        arr = []
        for index in idx:
            node = Node(index, nums[index])
            arr.append(node)
        i = 0
        j = len(arr) - 1
        while i < j:
            sumvalue = arr[i].value + arr[j].value
            if sumvalue < target:
                i = i + 1
            elif sumvalue > target:
                j = j - 1
            elif sumvalue == target:
                return [arr[i].index, arr[j].index]


class Node(object):
    def __init__(self, index=0, value=0):
        self.index = index
        self.value = value