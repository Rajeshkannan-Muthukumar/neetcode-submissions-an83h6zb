class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[-1]
        prof=0
        for i in range(len(prices)-2,-1,-1):
            if prices[i]<curr:
                prof+=abs(prices[i]-curr)
            curr=prices[i]
        return prof
