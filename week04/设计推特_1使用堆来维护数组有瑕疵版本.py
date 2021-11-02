# linkfor: https://leetcode-cn.com/problems/design-twitter/
from typing import List

from typing import List


class Artical:

    def __init__(self, userId, articalID, timeCount):
        self.userId = userId
        self.articalID = articalID
        self.timeCount = timeCount


class Heap:
    def __init__(self):
        self.content = []
        self.content.append(Artical(0, 0, 0))  # heap index start from 1

    def size(self):
        return len(self.content) - 1

    def push(self, data):
        self.content.append(data)
        self.heapifyup(self.size())

    def deleteMin(self):
        data = self.content[1]
        self.content[1] = self.content[-1]
        self.content = self.content[:-1]
        self.heapifydown(1)
        return data

    def heapifyup(self, index):
        while index > 1:
            data_cur = self.content[index]
            index_p = int(index / 2)
            data_p = self.content[index_p]
            if data_cur.timeCount < data_p.timeCount:
                self.content[index] = data_p
                self.content[index_p] = data_cur
                index = index_p
            else:
                break

    def heapifydown(self, index):
        child = index * 2
        while child <= self.size():
            child_oth = child + 1
            if child_oth <= self.size() and self.content[child].timeCount > self.content[child_oth].timeCount:
                child = child_oth
            if self.content[index].timeCount > self.content[child].timeCount:
                self.swap(index, child)
                index = child
                child = index * 2
            else:
                break

    def swap(self, index_1, index_2):
        num = self.content[index_1]
        self.content[index_1] = self.content[index_2]
        self.content[index_2] = num


class Twitter:

    def __init__(self):
        self.userViewArticle = {}
        self.userSendArticle = {}
        self.userContent = {}
        self.index = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        artical = Artical(userId, tweetId, self.index)
        for user in self.userViewArticle[userId]:
            heap = self.userContent.get(user, Heap())
            heap.push(artical)
            if heap.size() > 10:
                heap.deleteMin()
            self.userContent[user] = heap
        userheap = self.userSendArticle.get(userId, Heap())
        userheap.push(artical)
        if userheap.size() > 10:
            userheap.deleteMin()
        self.userSendArticle[userId] = userheap
        self.index = self.index + 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.userContent.get(userId, None)
        list = []
        if heap:
            list.extend(heap.content[1:])
            list.sort(key=lambda item: item.timeCount, reverse=True)
        return [item.articalID for item in list]

    def follow(self, followerId: int, followeeId: int) -> None:
        follow = self.userViewArticle.get(followeeId, [])
        if follow.__contains__(followerId):
            return
        follow.append(followerId)
        self.userViewArticle[followeeId] = follow

        heap_viewer = self.userContent.get(followerId, Heap())
        heap_follower = self.userSendArticle.get(followeeId, Heap())
        for item in heap_follower.content[1:]:
            heap_viewer.push(item)
        while heap_viewer.size() > 10:
            heap_viewer.deleteMin()

        self.userContent[followerId] = heap_viewer
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follow = self.userViewArticle.get(followeeId, [])
        if follow:
            follow.remove(followeeId)
            for item in self.userContent.get(followerId, Heap()).content:
                if item.userId == followeeId:
                    self.userContent.get(followerId).content.remove(item)
            heap = Heap()
            for item in self.userContent.get(followerId, Heap()).content[1:]:
                heap.push(item)

            while heap.size() > 10:
                heap.deleteMin()

            self.userContent[followerId] = heap
        return


# ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
# [[],[1,5],[2,3],[1,101],[2,13],[2,10],[1,2],[1,94],[2,505],[1,333],[2,22],[1,11],[1,205],[2,203],[1,201],[2,213],[1,200],[2,202],[1,204],[2,208],[2,233],[1,222],[2,211],[1],[1,2],[1],[1,2],[1]]

twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
twitter.postTweet(1, 101)
twitter.postTweet(1, 13)
twitter.postTweet(1, 10)
twitter.postTweet(1, 2)
twitter.postTweet(1, 94)
twitter.postTweet(1, 505)
twitter.postTweet(1, 333)
twitter.postTweet(1, 22)
twitter.postTweet(1, 11)
twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)
