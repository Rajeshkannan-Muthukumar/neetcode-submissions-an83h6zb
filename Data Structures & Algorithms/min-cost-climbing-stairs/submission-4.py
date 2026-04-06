class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res=[cost[0],cost[1]]
        for i in range(2,len(cost)):
            res.append(min(cost[i]+res[-1],cost[i]+res[-2]))
        return min(res[-1],res[-2])