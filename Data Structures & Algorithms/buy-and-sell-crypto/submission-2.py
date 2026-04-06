class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxiprof=0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            else:
                currprof=prices[i]-mini
                maxiprof=max(currprof,maxiprof)
        return maxiprof

