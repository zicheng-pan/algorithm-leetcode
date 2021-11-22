import math


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum = {}
        sum[(0, 0)] = 0
        for index in range(len(triangle)):
            for j in range(index + 1):
                if index == 0:
                    sum[(index,j)] = triangle[0][j]
                    continue
                if j == 0 :
                    sum[(index - 1, j - 1)] = math.pow(10,4)

                if j == index:
                    sum[(index - 1, j )] = math.pow(10, 4)

                sum[(index, j)] = min(sum[(index - 1, j - 1)], sum[(index - 1, j)]) + triangle[index][j]
        ans = math.pow(10,4)
        for item in sum.keys():
            if item[0] == len(triangle) - 1:
                ans = min(sum[item], ans)
        return ans

solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))