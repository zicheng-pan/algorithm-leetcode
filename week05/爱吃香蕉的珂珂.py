import math
from typing import List


def calc(weights, mid):
    ans = 0
    for weight in weights:
        ans = ans + math.ceil(weight/mid)
    return ans


class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        while left < right:
            mid = int((left + right) / 2)
            time = calc(piles, mid)
            if time <= h:
                right = mid
            else:
                left = mid + 1

        return right

solution = Solution()
print(solution.minEatingSpeed([312884470],
312884469))