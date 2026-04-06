class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1=None
        maj2=None
        cnt1=0
        cnt2=0
        thres=len(nums)//3
        major=[]
        for n in nums:
            if maj1 is None:
                maj1=n
                cnt1+=1
            elif maj2 is None and n!=maj1:
                maj2=n
                cnt2+=1
            elif n==maj1:
                cnt1+=1
            elif n==maj2:
                cnt2+=1
            else:
                if cnt1<cnt2:
                    cnt1-=1
                else:
                    cnt2-=1
                if cnt1==0:
                    maj1=n
                    cnt1+=1
                elif cnt2==0:
                    maj2=n
                    cnt2+=1
        fcnt1=0
        fcnt2=0
        for i in nums:
            if i==maj1:
                fcnt1+=1
            elif i==maj2:
                fcnt2+=1
        if fcnt1>thres:
            major.append(maj1)
        if fcnt2>thres:
            major.append(maj2)
        return major
