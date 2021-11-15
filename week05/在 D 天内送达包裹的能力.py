from typing import List


def calcdays(weights, mid):
    days = 0
    boate_weight = 0
    for weight in weights:
        boate_weight = boate_weight + weight
        if boate_weight > mid:
            days = days + 1
            boate_weight = weight

    days = days + 1
    return days


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min = 1
        max = 0

        for weight in weights:
            if weight > min:
                min = weight
            max = max + weight

        left = min
        right = max
        while left < right:
            mid = int((left + right) / 2)
            day = calcdays(weights, mid)
            if day <= days:
                right = mid
            else:
                left = mid + 1

        return right


solution = Solution()
solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)