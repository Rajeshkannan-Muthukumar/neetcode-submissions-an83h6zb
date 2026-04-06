class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        seen.add(n)
        while True:
            res=0
            while n>0:
                rem=n%10
                res+=rem**2
                n=n//10
            if res==1:
                return True
            if res in seen:
                return False
            seen.add(res)
            n=res
    # return True