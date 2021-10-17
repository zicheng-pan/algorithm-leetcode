# linkfor:https://leetcode-cn.com/problems/degree-of-an-array/
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        map = {}
        for num in nums:
            result = map.get(num, [])
            if result:
                result[0] = result[0] + 1
                result[2] = index
                map[num] = result

            else:
                result = []
                result.append(1)
                result.append(index)
                result.append(index)
                map[num] = result
            index = index + 1
        max = 0
        return_value = len(nums)
        for key in map.keys():
            if max < map.get(key)[0]:
                max = map.get(key)[0]
        for key in map.keys():
            if map.get(key)[0] == max:
                value = map.get(key)[2] - map.get(key)[1] + 1
                if value < return_value:
                    return_value = value

        return return_value



solution = Solution()
print(solution.findShortestSubArray(
    [1, 2, 2, 3, 1]))
