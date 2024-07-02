class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId) 
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)








### Intuition and Approach

# The problem requires implementing a Twitter-like service where users can post tweets, follow other users, and get a feed of the most recent tweets from the users they follow. 

# Here’s a step-by-step breakdown of how to approach this:

# 1. **Data Structures**:
#    - **`tweetMap`**: A dictionary mapping each user to a list of their tweets. Each tweet is represented by a tuple (timestamp, tweetId).
#    - **`followMap`**: A dictionary mapping each user to a set of users they follow.
#    - **`count`**: A global timestamp counter, decremented with each new tweet to maintain the order of tweets.

# 2. **Operations**:
#    - **Post Tweet**:
#      - Append the tweet with the current timestamp to the user’s list of tweets.
#    - **Get News Feed**:
#      - Collect the latest tweets from the user and the users they follow.
#      - Use a min-heap to maintain the most recent 10 tweets based on the timestamp.
#    - **Follow**:
#      - Add the followee to the follower's follow set.
#    - **Unfollow**:
#      - Remove the followee from the follower's follow set.

# ### Implementation

# ```python
# from collections import defaultdict
# import heapq
# from typing import List

# class Twitter:

#     def __init__(self):
#         self.count = 0
#         self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
#         self.followMap = defaultdict(set)  # userId -> set of followeeIds

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self.tweetMap[userId].append([self.count, tweetId])
#         self.count -= 1

#     def getNewsFeed(self, userId: int) -> List[int]:
#         res = []
#         minHeap = []
        
#         self.followMap[userId].add(userId)  # Ensure the user follows themselves
#         for followeeId in self.followMap[userId]:
#             if followeeId in self.tweetMap:
#                 index = len(self.ttweetMap[followeeId]) - 1
#                 count, tweetId = self.tweetMap[followeeId][index]
#                 minHeap.append([count, tweetId, followeeId, index - 1])
#         heapq.heapify(minHeap)
        
#         while minHeap and len(res) < 10:
#             count, tweetId, followeeId, index = heapq.heappop(minHeap)
#             res.append(tweetId)
#             if index >= 0:
#                 count, tweetId = self.tweetMap[followeeId][index]
#                 heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
#         return res

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.followMap[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         if followeeId in self.followMap[followerId]:
#             self.followMap[followerId].remove(followeeId)


# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)
# ```

# ### Explanation:

# 1. **Initialization (`__init__` method)**:
#    - Initialize `count` to track the global timestamp.
#    - Use `defaultdict` to initialize `tweetMap` and `followMap`.

# 2. **Post Tweet (`postTweet` method)**:
#    - Append the tweet with the current timestamp to the user’s tweet list.
#    - Decrement the global timestamp.

# 3. **Get News Feed (`getNewsFeed` method)**:
#    - Add the user themselves to their follow set.
#    - Collect the most recent tweet from each followed user and add to the min-heap.
#    - Extract the most recent 10 tweets using the heap.
   
# 4. **Follow (`follow` method)**:
#    - Add the followee to the follower’s follow set.

# 5. **Unfollow (`unfollow` method)**:
#    - Remove the followee from the follower’s follow set if present.

# This approach ensures efficient tweet posting, following, and unfollowing, and provides a way to retrieve the most recent tweets in the user's news feed using a min-heap for efficient sorting.