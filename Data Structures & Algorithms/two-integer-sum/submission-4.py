class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=l+1
        while l<len(nums):
            while r<len(nums):
                if nums[l]+nums[r]==target:
                    return[l,r]
                else:
                    r+=1
            l+=1
            r=l+1
        