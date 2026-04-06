class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=-1
        buy=prices[0]
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            curr=prices[i]-buy
            max_profit=max(max_profit,curr)
        return max_profit
