class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stck=[]
        prof=0
        for i in range(len(prices)-1,-1,-1):
            if not stck:
                stck.append(prices[i])
            else:
                if prices[i]<stck[-1]:
                    prof+=abs(prices[i]-stck[-1])
                    stck.pop()
                    stck.append(prices[i])
                else:
                    stck.pop()
                    stck.append(prices[i])
        return prof
