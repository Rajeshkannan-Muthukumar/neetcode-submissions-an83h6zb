class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        robbed=[nums[0],nums[1]]
        if nums[0]>nums[1]:
            fmax=nums[0]
            smax=nums[1]
            idx=0
        else:
            fmax=nums[1]
            smax=nums[0]
            idx=1
        # fmax=max(robbed)
        for i in range(2,len(nums)):
            if idx!=i-1:
                robbed.append(nums[i]+fmax)
            else:
                robbed.append(nums[i]+smax)
            if robbed[-1]>fmax:
                fmax,smax=robbed[-1],fmax
                idx=i
        return max(robbed[-1],robbed[-2])