# (Artical(0, 0),ArticalList())
from typing import List
import operator


class Heap:
    def __init__(self, compareFunction):
        self.content = []
        self.content.append(None)  # heap index start from 1
        self.compareFunction = compareFunction

    def size(self):
        return len(self.content) - 1

    def push(self, data):
        self.content.append(data)
        self.heapifyup(self.size())

    def getMax(self):
        return self.content[1]

    def deleteMax(self):
        if self.size() < 1:
            return
        data = self.content[1]
        self.content[1] = self.content[-1]
        self.content = self.content[:-1]
        self.heapifydown(1)
        return data

    def heapifyup(self, index):
        while index > 1:
            data_cur = self.content[index]
            index_p = int(index / 2)
            if self.compareFunction(data_cur, self.content[index_p]):
                self.swap(index, index_p)
                index = index_p
            else:
                break

    def heapifydown(self, index):
        child = index * 2
        while child <= self.size():
            child_oth = child + 1
            if child_oth <= self.size() and not self.compareFunction(self.content[child], self.content[child_oth]):
                child = child_oth
            if not self.compareFunction(self.content[index], self.content[child]):
                self.swap(index, child)
                index = child
                child = index * 2
            else:
                break

    def swap(self, index_1, index_2):
        num = self.content[index_1]
        self.content[index_1] = self.content[index_2]
        self.content[index_2] = num


class Artical:
    def __init__(self, id=None, index=None):
        self.id = id
        self.index = index
        self.next = None


def compareFunction(a: Artical, b: Artical):
    return a.index > b.index


class ArticalList:
    def __init__(self):
        self.head = Artical()


class UserArtical:
    def __init__(self):
        self.userArticals = {}
        self.index = 1

    def addUserArtical(self, userId: int, articalId: int):
        articallist = self.userArticals.get(userId, ArticalList())
        artical = Artical(articalId, self.index)
        self.index = self.index + 1
        head = articallist.head.next
        artical.next = head
        articallist.head.next = artical
        self.userArticals[userId] = articallist

    def getUserArticalList(self, userId: int):
        return self.userArticals.get(userId, ArticalList()).head


class Twitter:

    def __init__(self):
        self.followlist = {}
        self.userArtical = UserArtical()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.userArtical.addUserArtical(userId, tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 10
        heap = Heap(compareFunction)
        for item in self.followlist.get(userId,[]):
            artical = self.userArtical.getUserArticalList(item).next
            if artical:
                heap.push(artical)
        list = []
        while heap.size() > 0 and count >= 1:
            count = count - 1
            artical = heap.deleteMax()
            list.append(artical.id)
            if artical.next:
                heap.push(artical.next)
        return list

    def follow(self, followerId: int, followeeId: int) -> None:
        followl = self.followlist.get(followerId, [])
        if followl.__contains__(followeeId):
            return
        followl.append(followeeId)
        self.followlist[followerId] = followl
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followl = self.followlist.get(followerId, [])
        if followl.__contains__(followeeId):
            followl.remove(followeeId)
        return



arrayfunc = ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
             "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "follow",
             "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow", "follow",
             "follow", "getNewsFeed", "getNewsFeed", "getNewsFeed", "getNewsFeed", "getNewsFeed"]
arrayargs = [[], [1, 6765], [5, 671], [3, 2868], [4, 8148], [4, 386], [3, 6673], [3, 7946], [3, 1445], [4, 4822],
             [1, 3781], [4, 9038], [1, 9643], [3, 5917], [2, 8847], [1, 3], [1, 4], [4, 2], [4, 1], [3, 2], [3, 5],
             [3, 1], [2, 3], [2, 1], [2, 5], [5, 1], [5, 2], [1], [2], [3], [4], [5]]

# [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
#  null, null, null, null, null, null, null, [5917, 9643, 9038, 3781, 4822, 1445, 7946, 6673, 386, 8148],
#  [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765],
#  [8847, 5917, 9643, 3781, 1445, 7946, 6673, 2868, 671, 6765], [8847, 9643, 9038, 3781, 4822, 386, 8148, 6765],
#  [8847, 9643, 3781, 671, 6765]]
twitter = Twitter()
for item in range(1, len(arrayargs)):
    print(operator.methodcaller(arrayfunc[item], *arrayargs[item])(twitter))
