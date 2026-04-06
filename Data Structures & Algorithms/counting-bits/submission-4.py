class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        def bits(n):
            k=bin(n)[2:]
            cnt=0
            for i in k:
                if i=="1":
                    cnt+=1
            return cnt
        for i in range(n+1):
            res.append(bits(i))
        return res
        


        