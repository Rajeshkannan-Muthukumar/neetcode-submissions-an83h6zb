class Solution:
    def climbStairs(self, n: int) -> int:
        steps=[1,2]
        for i in range(2,n):
            steps.append(steps[-1]+steps[-2])
        return steps[n-1]