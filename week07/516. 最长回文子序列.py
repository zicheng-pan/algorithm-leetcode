class Solution(object):

    def __init__(self):
        self.substr = ""
        self.result = []

    def subString(self, s):
        self.result = []
        self.getsubString(s, 0)

    def getsubString(self, s, i):
        if i >= len(s):
            self.result.append(self.substr)
            return
        self.getsubString(s, i + 1)
        self.substr = self.substr + s[i]
        self.getsubString(s, i + 1)
        self.substr = self.substr[:-1]


    def ispalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        return True

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.subString(s)
        max_length = 0
        for str in self.result:
            if self.ispalindrome(str):
                max_length = max(max_length,len(str))

        return max_length


solution = Solution()
print(solution.longestPalindromeSubseq("aaaa"))
