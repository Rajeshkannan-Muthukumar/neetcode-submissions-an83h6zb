class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        # stck=[prices[-1]]
        mini=prices[0]
        for price in prices[1:]:
            if price>mini:
                prof+=price-mini
            mini=price
        return prof