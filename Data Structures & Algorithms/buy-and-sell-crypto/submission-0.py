class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        curr_profit=0
        min_price=prices[0]
        for p in prices:
            curr_profit=p-min_price
            max_profit=max(curr_profit,max_profit)
            min_price=min(min_price,p)
        return max_profit
        