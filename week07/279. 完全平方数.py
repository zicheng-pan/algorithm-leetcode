class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                array[i] = min(array[i], array[i - j * j] + 1)
                j = j + 1

        return array[n]


# 6730
solution = Solution()
print(solution.numSquares(6110))
