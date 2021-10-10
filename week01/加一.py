# linkfor : https://leetcode-cn.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits:
            result = digits[-1] + 1
            if result >= 10:
                temp = self.plusOne(digits[:-1])
                temp.append( result - 10)
                return temp
            else:
                digits[-1] = result
                return digits
        else:
            digits.insert(0, 1)
        return digits