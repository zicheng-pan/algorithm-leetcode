# linkfor: https://leetcode-cn.com/problems/maximal-rectangle/submissions/
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix_count = [[] for num in range(len(matrix))]
        index = 0
        for row in matrix:
            for inner_index in range(len(row)):
                if len(matrix_count[index]) > 0 and row[inner_index] == "1":
                    matrix_count[index].append(matrix_count[index][inner_index - 1] + 1)
                else:
                    matrix_count[index].append(int(matrix[index][inner_index]))
            index = index + 1
        print(str(matrix_count))

        column = []
        index = 0
        max_answer = 0
        if matrix_count:
            column_count = len(matrix_count[0])
            for index in range(column_count):
                for row in matrix_count:
                    column.append(row[index])

                calc = Calc()
                max_answer = max(calc.largestRectangleArea(column), max_answer)
                column = []
        return max_answer


class Calc(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        ans = 0
        stack = []
        for height in heights:
            accumulatewidth = 0
            while len(stack) > 0 and stack[-1].height > height:
                accumulatewidth = accumulatewidth + stack[-1].width
                area = accumulatewidth * stack[-1].height
                ans = ans if ans > area else area
                stack.pop()
            stack.append(Area(accumulatewidth + 1, height))
        return ans


class Area(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height


solution = Solution()
print(solution.maximalRectangle(
    [])
)
