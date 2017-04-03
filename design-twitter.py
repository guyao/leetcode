"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Example

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

"""

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_post = {}
        self.user_recent_post = {}
        self.user_follow = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if not userId in self.user_post:
            self.createUser(userId)
        t = tuple([self.time, tweetId])
        self.user_post[userId].append(t)
        self.time += 1
    

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        from heapq import heappush, nlargest
        tmp = []
        f_lst = self.user_follow[userId] if userId in self.user_follow else []
        for u in f_lst:
            for t in self.user_post[u][-10:]:
                heappush(tmp, t)
        return [t for time, t in nlargest(10, tmp)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if not followeeId in self.user_post:
            self.createUser(followeeId)
        if not followerId in self.user_post:
            self.createUser(followerId)
        if followeeId not in self.user_follow[followerId]:
            self.user_follow[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if not followerId in self.user_follow:
            return
        if followeeId in self.user_follow[followerId] and followeeId != followerId:
            self.user_follow[followerId].pop(self.user_follow[followerId].index(followeeId))

    def createUser(self, userId):
        self.user_post[userId] = []
        self.user_follow[userId] = [userId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



"""
Note:

Corner Case:
1. follow twice? ( follow self in default)
2. unfollow self?
    ["Twitter","postTweet","unfollow","getNewsFeed"]
    [[],[1,5],[1,1],[1]]
"""


#Test
"""
twitter = Twitter()
methods = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","unfollow","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","getNewsFeed","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","unfollow","getNewsFeed","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","unfollow","getNewsFeed","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet"]
args = [[],[11,994],[4,303],[1,113],[18,309],[8,905],[6,605],[1,210],[15,15],[1,88],[1,704],[8],[9,59],[4,851],[13,974],[2,133],[15,255],[15,662],[16,21],[13,227],[17],[5,603],[10,7],[5,816],[7,792],[12,260],[5],[4,586],[1,645],[20],[15,171],[16,18],[3,812],[15,153],[12,726],[6,508],[17,817],[5,6],[3,667],[5,599],[13,353],[11,282],[7,226],[18,423],[13,875],[2,738],[6,727],[7,374],[19,811],[8,418],[2,179],[3,476],[9,15],[16,8],[19,827],[17,203],[13,246],[14,8],[13,750],[4,595],[1,793],[17,995],[11,589],[2,115],[18,870],[15,426],[18,953],[10,318],[10,419],[2,164],[9],[18,854],[3,394],[17],[4,834],[4,349],[2,16],[13,534],[3,773],[4,292],[5,951],[17,554],[4,646],[6,412],[15,548],[8,188],[5,539],[18,732],[8,591],[11,733],[1,517],[8,156],[13,331],[11,889],[12,782],[11],[2,578],[16,487],[12,640],[14,112],[10,901],[8,807],[7,818],[7,627],[14,9],[4,522],[7,505],[9,13],[3],[1,971],[18,808],[1,17],[7,197],[7,361],[2,986],[17,6],[7,211],[15,342],[5,538],[1,711],[11,863],[17,339],[5,656],[4,402],[1,514],[11,566],[12,11],[12],[19,899],[19,526],[20,799],[4,1],[17,363],[7,845],[15,329],[17,369],[18,18],[15,848],[5,928],[18,105],[18],[17,785],[11,457]]

for m, arg in zip(methods[1:], args[1:]):
    f = getattr(twitter, m)
    print(m, arg)
    f(*tuple(arg))
"""