
class User:

    def __init__(self, following, tweets, userId):
        self.following = following
        self.tweets = tweets 
        self.userId = userId

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
        


    def postTweet(self, userId: int, tweetId: int) -> None:


        if userId not in self.users:
            newUser = User({}, [], userId)
            self.users[userId] = newUser

        self.users[userId].tweets.append((tweetId, self.time))
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        
        curUser = self.users[userId]
        res = []
        heap = []
        
        # Seed heap with the latest tweet from self + each followee
        sources = list(curUser.following.values())
        if curUser not in sources:
            sources.append(curUser)
        for user in sources:
            if user.tweets:
                idx = len(user.tweets) - 1
                tweetId, time = user.tweets[idx]
                heapq.heappush(heap, (-time, tweetId, idx, user))
        
        # Pop 10 times, pushing each user's next-older tweet after popping theirs
        for _ in range(min(10, len(heap) * 10)):
            if not heap:
                break
            neg_time, tweetId, idx, user = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                next_idx = idx - 1
                next_tweetId, next_time = user.tweets[next_idx]
                heapq.heappush(heap, (-next_time, next_tweetId, next_idx, user))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.users:
            newUser = User({}, [], followerId)
            self.users[followerId] = newUser

        if followeeId not in self.users:
            newUser = User({}, [], followeeId)
            self.users[followeeId] = newUser
        
        follower = self.users[followerId]
        followee = self.users[followeeId]

        if followee in follower.following:
            return
        
        follower.following[followeeId] = followee

    def unfollow(self, followerId: int, followeeId: int) -> None:

          
        if followerId not in self.users:
            newUser = User({}, [], followerId)
            self.users[followerId] = newUser
            return        

        if followeeId not in self.users:
            newUser = User({}, [], followeeId)
            self.users[followeeId] = newUser
            return 
        
        follower = self.users[followerId]

        if followeeId not in follower.following:
            return 

        followee = self.users[followeeId]
        
        follower.following.pop(followeeId)

        
