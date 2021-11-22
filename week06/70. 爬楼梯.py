class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        array = [0 for _ in range(n + 1)]
        for index in range(len(array)):
            if index == 0:
                array[index] = 0
                continue
            elif index == 1:
                array[index] = 1
                continue
            elif index == 2:
                array[index] = 2
                continue
            array[index] = array[index - 1] + array[index - 2]

        return array[n]