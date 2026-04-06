class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        res=[]
        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
        for j in range(len(nums)-2,-1,-1):
            right.append(right[-1]*nums[j+1])
        right=right[::-1]
        for k in range(len(nums)):
            res.append(left[k]*right[k])
        return res