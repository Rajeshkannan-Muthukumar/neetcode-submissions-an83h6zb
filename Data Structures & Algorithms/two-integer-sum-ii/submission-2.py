class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # def helper(nums,target):
        #     i=0
        #     j=len(numbers)-1
        #     nums=nums
        #     while i<j:
        #         m=i+(j-i)//2
        #         if nums[m]==target:
        #             return m
        #         elif nums[m]<target:
        #             i=m+1
        #         else:
        #             j=m-1
        #     return i
        k=0
        z=len(numbers)-1
        while k<z:
            if numbers[k]+numbers[z]==target:
                return [k+1,z+1]
            elif numbers[k]+numbers[z]>target:
                z-=1
            else:
                k+=1
        return [-1,-1]