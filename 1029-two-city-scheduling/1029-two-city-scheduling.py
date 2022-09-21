class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # sort by the diff
        # keep cost_a before cost_b 
        # send first n/2 folks to A and the remaining to B
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        n = len(costs)//2
        
        total_cost = 0
        
        for i in range(n):
            total_cost+= costs[i][0] + costs[i+n][1]
        
        return total_cost