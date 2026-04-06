class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0,1]
        def bits(n):
            ctr=0
            while n!=0:
                ctr+=(n&1)
                n=n>>1
            return ctr
        for i in range(2,n+1):
            res.append(bits(i))
        return res[:n+1]

        