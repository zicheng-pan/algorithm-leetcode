# linkfor:https://leetcode-cn.com/problems/sliding-window-maximum/
import collections

from week01.设计循环双端队列 import MyCircularDeque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dequeue = MyCircularDeque(k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []
        for index in range(len(nums)):

            while not dequeue.isEmpty() and dequeue.getFront() < index + 1 - k:
                dequeue.deleteFront()
            while not dequeue.isEmpty() and nums[dequeue.getRear()] < nums[index]:
                dequeue.deleteLast()
            dequeue.insertLast(index)
            if not dequeue.isEmpty() and index + 1 - k >= 0:
                answer.append(nums[dequeue.getFront()])
        return answer


solution = Solution()
solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)