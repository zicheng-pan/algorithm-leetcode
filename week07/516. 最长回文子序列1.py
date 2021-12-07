class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        item = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            item[i][i] = 1

        result = 0

        for i in range(length):
            for j in range(length):
                count = 0
                index_y = j
                if i - 1 < 0:
                    index_x = 0
                else:
                    index_x = i - 1
                    count = count + 1
                if index_y +1 > length - 1:
                    index_y = length - 1
                else:
                    index_y = j + 1
                    count = count + 1
                if s[index_x] == s[index_y]:
                    item[index_x][index_y] = item[i][j] + count
                else:
                    item[index_x][index_y] = max(item[index_x][j], item[i][index_y])

                result = max(result,item[index_x][index_y])

        return result


solution = Solution()
print(solution.longestPalindromeSubseq("aabaa"))
