# linkfor: https://leetcode-cn.com/problems/subarray-sum-equals-k/
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = []
        sum.append(0)
        for index, num in enumerate(nums):
            sum.append(sum[index] + num)
        return self.subscribtion(sum, k)

    def subscribtion(self, arr, k):
        resultMap = {}
        resultlist = []
        count = 0
        for item in arr:
            key = item - k
            if resultMap.get(key, None) != None:
                count = count + resultMap.get(key)
                resultlist.append(key)
            resultMap[item] = resultMap.get(item, 0) + 1
        return count


solution = Solution()
print(solution.subarraySum([1, -1, 0], 0))
