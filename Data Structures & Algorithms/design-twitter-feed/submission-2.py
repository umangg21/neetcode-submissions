class Twitter:

    def __init__(self):
        self.followmap = {}
        self.tweetmap = {}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweetmap:
            self.tweetmap[userId] = []
        
        self.count+=1
        self.tweetmap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = []
        
        usersTweets = self.tweetmap[userId] if userId in self.tweetmap else []
        if usersTweets:
            allTweets.extend(usersTweets)
        
        followers = self.followmap[userId] if userId in self.followmap else []

        if followers:
            for follower in followers:
                followerTweets = self.tweetmap[follower]
                if followerTweets:
                    allTweets.extend(followerTweets)


        heapq.heapify_max(allTweets)
        news_count = 10
        final_feed = []

        while news_count > 0 and len(allTweets)>0:
            news_count -=1
            feed = heapq.heappop_max(allTweets)
            final_feed.append(feed[1])
        
        return final_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            return
        self.followmap[followerId].discard(followeeId)