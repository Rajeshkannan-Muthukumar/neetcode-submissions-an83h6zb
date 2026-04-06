class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles,d):
            clm=0
            for n in piles:
                num=n//d
                rem=1 if n%d !=0 else 0
                clm+=num+rem
            return clm
        piles.sort()
        l=1
        r=max(piles)
        while l<r:
            m=l+(r-l)//2
            hrs=hours(piles,m)
            if hrs<=h:
                r=m
            else:
                l=m+1
        return l
