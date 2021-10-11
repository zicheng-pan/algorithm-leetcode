#linkfor https://leetcode-cn.com/problems/design-circular-deque/
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.maxcount = k
        self.arr = []


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.arr.insert(0,value)
            return True
        else:
            return False


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.arr.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            del self.arr[0]
            return True
        else:
            return False


    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            del self.arr[-1]
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.arr[0]
        else :
            return -1


    def getRear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1


    def isEmpty(self):
        """
        :rtype: bool
        """

        return len(self.arr) == 0


    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.arr) == self.maxcount