class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        # stck=[prices[-1]]
        maxi=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i]<maxi:
                prof+=(maxi-prices[i])
            maxi=prices[i]
        return prof
