# linkfor : https://leetcode-cn.com/problems/count-of-range-sum/
from typing import List


class Solution:

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.ans = 0
        array = []
        array.append(0)
        for item in nums:
            array.append(array[-1] + item)

        self.mergeSort(array, 0, len(array) - 1)
        return self.ans

    def mergeSort(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        mid = (l + r) >> 1
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        self.caculate(nums, l, mid, r)
        self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        arr = [0 for _ in range(r - l + 1)]
        i = l
        j = mid + 1
        for index in range(len(arr)):
            if j > r or (i <= mid and nums[i] <= nums[j]):
                arr[index] = nums[i]
                i = i + 1
            else:
                arr[index] = nums[j]
                j = j + 1
        for index in range(len(arr)):
            nums[l + index] = arr[index]

    def caculate(self, nums, l, mid, r):
        i = l
        left_start = mid + 1
        left_end = mid + 1
        while i <= mid:
            while left_start <= r and nums[left_start] - nums[i] < self.lower:
                left_start = left_start + 1
            while left_end <= r and nums[left_end] - nums[i] <= self.upper:
                left_end = left_end + 1
            self.ans = left_end - left_start + self.ans
            i = i + 1


solution = Solution()
print(solution.countRangeSum([-2, 5, -1],
                             -2,
                             2))
