class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return 0
        max_index = 0
        length = len(nums)
        ans = [0 for _ in range(length)]

        for i in range(len(ans)):
            if i <= max_index:
                for j in range(nums[i] + 1):
                    ans[i] = max(j + i, ans[i])

                max_index = max(max_index, ans[i])
                if max_index + 1 >= length:
                    break


soluton = Solution()
print(soluton.jump([1,2,1,1,1]))
print(soluton.jump(
[2,3,1,1,4]))
print(soluton.jump([2,3,0,1,4]
))
