class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxcon=0
        while i<j:
            curr=(j-i)*min(heights[i],heights[j])
            maxcon=max(curr,maxcon)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxcon