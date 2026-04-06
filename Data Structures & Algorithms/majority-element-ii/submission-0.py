class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        maxcnt=len(nums)//3
        cnt=0
        major=[]
        i=0
        j=0
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                cnt=j-i
                if cnt>maxcnt:
                    major.append(nums[i])
                i=j
        cnt=j-i
        if cnt>maxcnt:
            major.append(nums[i])
        return major