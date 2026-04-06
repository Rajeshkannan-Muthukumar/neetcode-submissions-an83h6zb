class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        maj=-1
        for n in nums:
            if count==0:
                maj=n
                count+=1
            elif maj==n:
                count+=1
            else:
                count-=1
        return maj
