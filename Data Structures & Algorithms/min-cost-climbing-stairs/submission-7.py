class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        fir=cost[0]
        sec=cost[1]
        for i in range(2,len(cost)):
            temp=min(fir+cost[i],sec+cost[i])
            fir=sec
            sec=temp
        return min(fir,sec)