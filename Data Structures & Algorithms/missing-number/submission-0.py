class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for n in nums:
            s+=n
        l=len(nums)
        act_sum=l*(l+1)//2
        return act_sum-s
        