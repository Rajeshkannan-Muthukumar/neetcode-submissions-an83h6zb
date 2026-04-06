class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(nums,l,r,target):
            while l<r:
                m=l+(r-l)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m
            if nums[l]==target:
                return l
            return -1
        def minidx(nums):
            l=0
            r=len(nums)-1
            while l<r:
                m=l+(r-l)//2
                if nums[m]>nums[r]:
                    l=m+1
                else:
                    r=m
            return l
        l=minidx(nums)
        r=len(nums)-1
        if nums[r]<target:
            return bsearch(nums,0,l-1,target)
        else:
            return bsearch(nums,l,r,target)
  
