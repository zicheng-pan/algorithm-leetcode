#linkfor https://leetcode-cn.com/problems/design-circular-deque/
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.maxcount = k
        self.count = 0
        self.arr = []


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        print(str(self.arr))
        print("insert value ="+str(value))
        if not self.isFull():
            self.arr.append(0)
            self.count = len(self.arr)
            for index in range(1,self.count).__reversed__():
                print(index)
                self.arr[index] = self.arr[index - 1]
            self.arr[0] = value

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
            self.count = len(self.arr)
            return True
        else:
            return False

    def deleteFront(self):
        """
        :rtype: bool
        """

        if not self.isEmpty():
            self.arr = self.arr[1:]
            self.count = len(self.arr)
            return True
        else:
            return False


    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.arr = self.arr[:-1]
            self.count = len(self.arr)
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if self.count > 0:
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