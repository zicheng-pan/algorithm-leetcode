import sys


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        for index in range(len(nums)):
            for j in range(index):
                if nums[j] < nums[index]:
                    if arr[j] + 1 > arr[index]:
                        count[index] = count[j]
                    elif arr[j] + 1 == arr[index]:
                        count[index] = count[j] + count[index]
                    arr[index] = max(arr[j] + 1, arr[index])

        max_count = -sys.maxsize - 1
        for item in arr:
            max_count = max(max_count, item)

        ans = 0
        for index in range(len(arr)):
            if arr[index] == max_count:
               ans = ans + count[index]
        return ans

solution = Solution()
print(solution.findNumberOfLIS(
[1,2,4,3,5,4,7,2]))