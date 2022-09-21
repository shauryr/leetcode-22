class Leaderboard:
    from collections import defaultdict
    def __init__(self):
        self.dict_scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.dict_scores:
            self.dict_scores[playerId] = 0
        self.dict_scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for _,v in self.dict_scores.items():
            heappush(heap, -v)
        
        result = 0
        
        while K>0:
            result+= -heappop(heap)
            K-=1
        
        return result
            

    def reset(self, playerId: int) -> None:
        self.dict_scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)