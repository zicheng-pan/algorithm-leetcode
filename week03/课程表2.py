# linkfor: https://leetcode-cn.com/problems/course-schedule-ii/submissions/
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        to = {}
        inDeg = [0 for _ in range(numCourses)]

        for list in prerequisites:
            to_list = to.get(list[1], [])
            to_list.append(list[0])
            to[list[1]] = to_list
            inDeg[list[0]] = inDeg[list[0]] + 1

        queue = []

        for index in range(numCourses):
            if inDeg[index] == 0:
                queue.append(index)

        lessons = []
        while queue:
            course = queue[0]
            del queue[0]
            lessons.append(course)

            for item in to.get(course,[]):
                inDeg[item] = inDeg[item] - 1

                if inDeg[item] == 0:
                    queue.append(item)
        if len(lessons) == numCourses:

            return lessons
        return []