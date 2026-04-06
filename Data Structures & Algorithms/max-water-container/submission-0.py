class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rec=float("-inf")
        l=0
        r=len(heights)-1
        while l<r:
            leng=min(heights[l],heights[r])
            wid=r-l
            area=leng*wid
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            rec=max(area,rec)

        return rec
