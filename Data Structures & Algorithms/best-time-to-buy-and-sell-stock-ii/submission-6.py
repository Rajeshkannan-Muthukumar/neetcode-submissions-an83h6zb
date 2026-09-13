class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        stck=[prices[-1]]
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>stck[-1]:
                stck.pop()
                stck.append(prices[i])
            else:
                prof+=(stck[-1]-prices[i])
                stck.pop()
                stck.append(prices[i])
        return prof