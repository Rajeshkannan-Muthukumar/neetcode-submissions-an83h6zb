class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        steps=[cost[0],cost[1]]
        for i in range(2,len(cost)):
            prev=steps[i-1]
            fprev=steps[i-2]
            steps.append(min(fprev+cost[i],prev+cost[i]))
        return min(steps[-1],steps[-2])