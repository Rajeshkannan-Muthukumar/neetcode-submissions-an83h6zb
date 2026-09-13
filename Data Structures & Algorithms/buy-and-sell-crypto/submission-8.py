class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highprof=0
        minip=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minip:
                minip=prices[i]
            else:
                highprof=max(highprof,prices[i]-minip)
        return highprof