class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                # left=[1]
        right=1
        res=[1]
        for i in range(1,len(nums)):
            res.append(res[-1]*nums[i-1])
        for j in range(len(nums)-2,-1,-1):
            right=right*nums[j+1]
                                                                                # for k in range(len(nums)):
            res[j]=res[j]*right
        return res
                                                                                                            
        