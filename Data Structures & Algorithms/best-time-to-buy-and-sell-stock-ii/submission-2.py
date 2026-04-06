class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stck=[prices[-1]]
        prof=0
        for i in range(len(prices)-2,-1,-1):
            if prices[i]<stck[-1]:
                prof+=abs(prices[i]-stck[-1])
            stck.append(prices[i])
        return prof
