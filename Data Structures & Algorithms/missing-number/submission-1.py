class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        exp=n*(n+1)//2
        return exp-s